import pandas as pd
from IDataExtractor import IDataExtractor

class ExtractCsv(IDataExtractor):
    def __init__(self, filepath: str, delimiter: str = ';'):
        self.filepath: str = filepath
        self.delimiter: str = delimiter

    def extract(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.filepath, delimiter=self.delimiter)
            return df
        except FileNotFoundError:
            print(f"Erreur: Fichier non trouvé à l'emplacement: {self.filepath}")
            return pd.DataFrame() 
        except pd.errors.EmptyDataError:
            print(f"Alerte: Fichier vide: {self.filepath}")
            return pd.DataFrame() 
        except Exception as e:
            print(f"Erreur inattendue lors de la lecture du CSV: {e}")
            return pd.DataFrame() 