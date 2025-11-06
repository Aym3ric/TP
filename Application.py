from IDataExtractor import IDataExtractor 
from DataTransformer import DataTransformer
from Visualizer import Visualizer
from ExtractCsv import ExtractCsv

class Application:
    def __init__(self):
        self.extractor: IDataExtractor
        self.transformer = DataTransformer()
        self.visualizer = Visualizer()

    def run(self):
        type_extract = self.visualizer.choice_type_extract()
        ville = self.visualizer.choice_ville()
        station = self.visualizer.choice_station(ville)
        
        if type_extract == "csv":
            extractor = ExtractCsv(f"{station}.csv")
            self.extractor = extractor
            
        df = self.extractor.extract()
        metriques = self.transformer.transform(df)
        self.visualizer.show_history(metriques)