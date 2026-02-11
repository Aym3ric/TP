"""
Module d'extraction de données depuis un fichier CSV.
"""
import pandas as pd
from services.i_data_extractor import IDataExtractor

class ExtractCsv(IDataExtractor):
    """
    Implémentation de l'extraction de données depuis un fichier CSV local.
    """
    def __init__(self, filepath: str, delimiter: str = ';'):
        """Initialise le chemin du fichier et le délimiteur."""
        self.filepath: str = filepath
        self.delimiter: str = delimiter

    def execute(self) -> pd.DataFrame:
        """
        Lit le fichier CSV et retourne un DataFrame pandas.

        Returns:
            pd.DataFrame: Les données brutes ou un DataFrame vide en cas d'erreur.
        """
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

# Command