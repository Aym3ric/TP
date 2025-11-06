from IDataExtractor import IDataExtractor 
from DataTransformer import DataTransformer
from Visualizer import Visualizer
from ExtractCsv import ExtractCsv
from Ville import Ville
from Station import Station
from typing import List

class Application:
    def __init__(self):
        self.transformer = DataTransformer()
        self.visualizer = Visualizer()
        self.extractor: IDataExtractor | None = None
        self.villes: List[Ville] = [] 
        
    def _setup_data(self):
        toulouse = Ville("Toulouse")
        villes = [toulouse]
        station_compans = Station("Compans Cafarelli")
        stations = [station_compans]

        for station in stations:
            toulouse.add_station(station)
        
        for ville in villes:
            self.villes.append(ville)
        
    def run(self):
        try:
            print("--- Configuration de la recherche ---")
            self._setup_data() 
            
            if not self.villes:
                print("Erreur: Aucune ville n'est configurée dans l'application.")
                return

            type_extract = self.visualizer.choice_type_extract()
            selected_ville: Ville = self.visualizer.choice_ville(self.villes)
            selected_station: Station = self.visualizer.choice_station(selected_ville)

            if type_extract == "csv":
                file_name = f"{selected_station.nom.lower()}.csv"
                self.extractor = ExtractCsv(file_name)
            else:
                print(f"Type d'extracteur '{type_extract}' non géré.")
                return
        
        except KeyboardInterrupt:
            print("\nConfiguration annulée.")
            return
            
        try:
            while True:
                print(f"\n--- Chargement des données pour {selected_station.nom} ---")
                df = self.extractor.extract()
                if df.empty:
                    print("Aucune donnée n'a été extraite (fichier vide ou non trouvé).")
                    

                metriques = []
                if not df.empty:
                    metriques = self.transformer.transform(df)
                
                if not metriques:
                    print("Aucune donnée valide n'a pu être transformée.")
                else:
                    self.visualizer.show_history(metriques)

                if not self.visualizer.ask_for_refresh():
                    break 

        except KeyboardInterrupt:
            print("\nApplication interrompue par l'utilisateur.")
        finally:
            print("Merci d'avoir utilisé l'application. Au revoir !")