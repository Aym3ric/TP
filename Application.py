from IDataExtractor import IDataExtractor 
from IDataTransformer import IDataTransformer 
from Visualizer import Visualizer
from ExtractCsv import ExtractCsv
from Ville import Ville
from Station import Station
from typing import List

class Application:
    
    def __init__(self, 
                 transformer: IDataTransformer, 
                 visualizer: Visualizer, 
                 villes: List[Ville]):
        
        self.transformer = transformer
        self.visualizer = visualizer
        self.villes = villes 
        self.extractor: IDataExtractor | None = None
        
    def run(self):
        try:
            print("--- Configuration de la recherche ---")
            
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