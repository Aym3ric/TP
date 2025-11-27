from services.IDataTransformer import IDataTransformer 
from ui.Visualizer import Visualizer
from services.ExtractCsv import ExtractCsv
from models.Station import Station
from structures.File import File
from structures.LinkedList import LinkedList
from structures.Maillon import Maillon

class Application:
    
    def __init__(self, 
                 transformer: IDataTransformer, 
                 visualizer: Visualizer, 
                 stations_config: dict):
        
        self.transformer = transformer
        self.visualizer = visualizer
        
        # Structure 1 : La File pour gérer les tâches d'extraction
        self.file_extraction = File()
        
        # Structure 2 : La Liste Chaînée pour stocker et parcourir les résultats
        self.liste_resultats = LinkedList()
        
        # On remplit la file d'attente au démarrage
        self._init_file_attente(stations_config)

    def _init_file_attente(self, config: dict):
        """Charge les tâches d'extraction dans la File."""

        print(f"Chargement de {len(config)} stations dans la file d'attente...")
        
        for nom_station, chemin_csv in config.items():
            task_data = {
                "nom_station": nom_station,
                "csv_path": chemin_csv
            }
        
            self.file_extraction.enfiler(task_data)

    def run(self):
        try:
            print("\n=== PHASE 1 : EXTRACTION DES DONNÉES (FILE) ===")
            
            while not self.file_extraction.est_vide():
                task = self.file_extraction.defiler()
                nom_station = task["nom_station"]
                csv_path = task["csv_path"]
                
                print(f"Traitement en cours : {nom_station}...")
                
                extractor = ExtractCsv(csv_path) #
                df = extractor.extract()
                
                if df.empty:
                    print(f"  -> Avertissement : Pas de données pour {nom_station}")
                    continue

                metriques = self.transformer.transform(df) 
                
                if metriques:
                    station_remplie = Station(nom_station) #
                    for m in metriques:
                        station_remplie.add_metrique(m)
                    
                    maillon_resultat = Maillon(station_remplie) #
                    self.liste_resultats.add_maillon(maillon_resultat)
                    print(f"  -> Succès : {len(metriques)} métriques chargées.")
                else:
                    print("  -> Erreur : Aucune métrique valide transformée.")

            
            print("\n=== PHASE 2 : VISUALISATION (LISTE CHAÎNÉE) ===")
            
            if self.liste_resultats.est_vide(): #
                print("Aucune station disponible à l'affichage.")
                return

            courant = self.liste_resultats.first_maillon
            
            while courant is not None:
                station_actuelle: Station = courant.val
                
                print(f"\n--- MÉTÉO POUR : {station_actuelle.nom} ---")
                self.visualizer.show_history(station_actuelle.metriques) #
                
                if courant.get_suiv() is not None:
                    choix = input("\n[Entrée] Station suivante | [Q] Quitter : ").strip().lower()
                    if choix == 'q':
                        break

                    courant = courant.get_suiv() #
                else:
                    print("\nFin de la liste des stations.")
                    break

        except KeyboardInterrupt:
            print("\nApplication interrompue.")
        finally:
            print("Au revoir !")