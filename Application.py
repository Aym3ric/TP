"""
Point d'entrée principal de la logique applicative.
"""
from services.i_data_transformer import IDataTransformer
from ui.visualizer import Visualizer
from services.extract_csv import ExtractCsv
from services.extract_api import ExtractApi
from models.station import Station
from models.ville import Ville
from structures.linked_list import LinkedList
from structures.file_structure import File
from ui.station_display_decorator import StationDisplayDecorator

class Application:
    """
    Contrôleur principal de l'application.
    Gère le flux de données entre l'extraction, la transformation et l'affichage.
    """

    def __init__(self,
                 transformer: IDataTransformer,
                 visualizer: Visualizer,
                 stations_config: dict):
        """
        Initialise l'application.

        Args:
            transformer (IDataTransformer): Service de transformation des données.
            visualizer (Visualizer): Service d'affichage et d'interaction utilisateur.
            stations_config (dict): Configuration des stations (URLs, chemins).
        """
        self.transformer = transformer
        self.visualizer = visualizer
        self.stations_config = stations_config

        self.villes = self._init_villes()

    def _init_villes(self) -> list[Ville]:
        """Initialise la ville de Toulouse avec les stations présentes dans la config (sans charger les données)."""
        toulouse = Ville("Toulouse")
        for nom_station in self.stations_config.keys():
            toulouse.add_station(Station(nom_station))
        return [toulouse]

    def _load_data(self, stations_linked_list: LinkedList, source_type: str):
        """Charge les données pour les stations (LinkedList) demandées selon la source."""
        print(f"\n--- CHARGEMENT DES DONNEES (Source: {source_type.upper()}) ---")

        current_maillon = stations_linked_list.first_maillon
        while current_maillon is not None:
            station = current_maillon.val

            if station.nom not in self.stations_config:
                print(f"  -> Erreur : Pas de configuration pour {station.nom}")
                current_maillon = current_maillon.get_suiv()
                continue

            config_station = self.stations_config[station.nom]

            if source_type not in config_station or not config_station[source_type]:
                print(f"  -> Erreur : Pas de source '{source_type}' configurée pour {station.nom}")
                current_maillon = current_maillon.get_suiv()
                continue

            source_path = config_station[source_type]

            try:
                if source_type == 'csv':
                    print(f"Chargement {station.nom} depuis CSV : {source_path}...")
                    extractor = ExtractCsv(source_path)
                elif source_type == 'api':
                    print(f"Chargement {station.nom} depuis API...")
                    extractor = ExtractApi(source_path)
                else:
                    print(f"Type de source inconnu : {source_type}")
                    current_maillon = current_maillon.get_suiv()
                    continue

                df = extractor.execute()

                if not df.empty:
                    # Transformation
                    metriques = self.transformer.transform(df)
                    if metriques:
                        station.metriques = metriques
                        print(f"  -> Succès : {len(metriques)} métriques chargées.")
                    else:
                        print(f"  -> Attention : Aucune métrique valide transformée pour {station.nom}")
                else:
                    print(f"  -> Attention : Données vides pour {station.nom}")

            except Exception as e:
                print(f"  -> Erreur lors du chargement de {station.nom}: {e}")

            current_maillon = current_maillon.get_suiv()

    def run(self):
        """Lance la boucle principale de l'application."""
        try:
            print("Bienvenue dans l'application Météo !")

            while True:
                print("\n=== ETAPE 1 : CHOIX DE LA VILLE ===")
                ville_choisie = self.visualizer.choice_ville(self.villes)

                while True:
                    print(f"\n=== ETAPE 2 : CHOIX DES STATIONS ({ville_choisie.nom}) ===")
                    stations_select_list = self.visualizer.choice_station(ville_choisie)

                    stations_linked_list = LinkedList()
                    for s in stations_select_list:
                        stations_linked_list.add(s)

                    print("\n=== ETAPE 3 : CHOIX DE LA SOURCE ===")
                    source_type = self.visualizer.choice_type_extract()

                    print("\n=== ETAPE 4 : CHARGEMENT DES DONNEES ===")
                    self._load_data(stations_linked_list, source_type)

                    print("\n=== ETAPE 5 : AFFICHAGE ===")

                    display_queue = File()
                    current_maillon = stations_linked_list.first_maillon
                    while current_maillon is not None:
                        display_queue.enfiler(current_maillon.val)
                        current_maillon = current_maillon.get_suiv()

                    while not display_queue.est_vide():
                        station = display_queue.defiler()
                        if station:
                            if station.metriques:
                                decorator = StationDisplayDecorator(station)
                                print(decorator.show())
                                print("-" * 30)
                            else:
                                print(f"\nPas de données à afficher pour {station.nom}")

                    print(f"\nConsulter d'autres stations de {ville_choisie.nom} ?")
                    if input(" (o/n) : ").lower().strip() != 'o':
                        break

                print("\nChanger de ville ?")
                if input(" (o/n) : ").lower().strip() != 'o':
                    break

        except KeyboardInterrupt:
            print("\nApplication interrompue.")
        finally:
            print("Au revoir !")
