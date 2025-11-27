from services.IDataTransformer import IDataTransformer 
from ui.Visualizer import Visualizer
from services.ExtractCsv import ExtractCsv
from models.Station import Station
from structures.LinkedList import LinkedList
from structures.Maillon import Maillon

class Application:
    
    def __init__(self, 
                 transformer: IDataTransformer, 
                 visualizer: Visualizer, 
                 stations_config: dict): 
        
        self.transformer = transformer
        self.visualizer = visualizer
        self.stations_structure = LinkedList()
        
        # Initialisation de la structure de données à partir du config
        self._init_stations(stations_config)

    def _init_stations(self, config: dict):
        """Remplit la liste chaînée avec les stations et leurs chemins CSV."""
        for nom_station, chemin_csv in config.items():
            station = Station(nom_station)
            
            data = {
                "station_obj": station,
                "csv_path": chemin_csv
            }
            
            self.stations_structure.add_maillon(Maillon(data))

    def run(self):
        try:
            print("--- Configuration de la recherche ---")
            
            items_a_traiter = self.stations_structure.to_list()
            
            if not items_a_traiter:
                print("Aucune station configurée.")
                return

            for item in items_a_traiter:
                station: Station = item["station_obj"]
                csv_path: str = item["csv_path"]
                
                print(f"\n--- Chargement des données pour {station.nom} ---")
                
                extractor = ExtractCsv(csv_path)
                df = extractor.extract() 
                
                if df.empty:
                    print("Aucune donnée n'a été extraite.")
                    continue
                    
                metriques = self.transformer.transform(df)
                
                if not metriques:
                    print("Aucune donnée valide transformée.")
                else:
                    self.visualizer.show_history(metriques)

                if not self.visualizer.ask_for_refresh():
                    break 

        except KeyboardInterrupt:
            print("\nApplication interrompue par l'utilisateur.")
        finally:
            print("Merci d'avoir utilisé l'application. Au revoir !")