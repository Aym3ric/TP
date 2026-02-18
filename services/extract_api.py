"""
Module d'extraction de données depuis une API (format JSON).
"""
import pandas as pd
import requests
from services.i_data_extractor import IDataExtractor

class ExtractApi(IDataExtractor):
    """
    Implémentation de l'extraction de données depuis une API JSON.
    """
    def __init__(self, url: str):
        """Initialise avec l'URL de l'API."""
        self.url = url

    def execute(self) -> pd.DataFrame:
        """Exécute la requête HTTP et retourne un DataFrame."""
        try:
            print(f"Connexion à l'API : {self.url} ...")
            response = requests.get(self.url, timeout=15)
            response.raise_for_status()

            data = response.json()

            if 'results' in data and isinstance(data['results'], list):
                df = pd.DataFrame(data['results'])
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                print("Format JSON inattendu.")
                return pd.DataFrame()

            if df.empty:
                return df

            df.columns = df.columns.str.strip().str.lower()

            selected_cols = self._identify_columns(df.columns)

            if not selected_cols:
                print("Attention: Aucune colonne météo identifiée.")
                return pd.DataFrame()

            df = df[list(selected_cols.keys())].copy()
            df.rename(columns=selected_cols, inplace=True)

            return df

        except Exception as e:
            print(f"Erreur lors de l'extraction API : {e}")
            return pd.DataFrame()

    def _identify_columns(self, columns):
        """Identifie les colonnes pertinentes dans le DataFrame."""
        selected_cols = {}

        temp_col = self._find_col(['temperature', 'temperature_en_degre_c', 'temp_c', 't'], columns)
        if temp_col:
            selected_cols[temp_col] = 'temperature'

        pres_col = self._find_col(['pression', 'pression_au_niveau_mer', 'pres', 'p'], columns)
        if pres_col:
            selected_cols[pres_col] = 'pression'

        hum_col = self._find_col(['humidite', 'humimidite', 'hum', 'u'], columns)
        if hum_col:
            selected_cols[hum_col] = 'humidite'

        date_col = self._find_col(['heure_utc', 'date', 'timestamp', 'time'], columns)
        if date_col:
            selected_cols[date_col] = 'heure_utc'

        return selected_cols

    def _find_col(self, candidates: list[str], columns):
        """Cherche une colonne candidate dans la liste des colonnes disponibles."""
        for cand in candidates:
            if cand in columns:
                return cand

        for cand in candidates:
            for col in columns:
                if cand in col:
                    return col
        return None
