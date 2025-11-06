import pandas as pd
from IDataExtractor import IDataExtractor

class ExtractCsv(IDataExtractor):
    def __init__(self, filepath: str, delimiter: str = ';'):
        self.filepath: str = filepath
        self.delimiter: str = delimiter

    def extract(self):
        df = pd.read_csv(self.filepath, delimiter=self.delimiter)
        return df