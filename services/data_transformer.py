"""
Module de transformation des données brutes en objets Metrique.
"""
from typing import List
import pandas as pd
from services.i_data_mapper import IDataMapper
from services.i_data_transformer import IDataTransformer
from models.metrique import Metrique

class DataTransformer(IDataTransformer):
    """
    Classe responsable de la transformation et du nettoyage des DataFrames.
    """

    def __init__(self, mapper: IDataMapper):
        """Initialise le transformer avec un mapper."""
        self.mapper = mapper

    def transform(self, df: pd.DataFrame) -> List[Metrique]:
        """
        Nettoie le DataFrame et le transforme en liste de métriques.

        Args:
            df (pd.DataFrame): DataFrame brut issu de l'extraction.

        Returns:
            List[Metrique]: Liste d'objets Metrique valides.
        """
        date_col = 'heure_utc'
        temp_col = 'temperature'
        humid_col = 'humidite'
        press_col = 'pression'

        required_cols = [date_col, temp_col, humid_col, press_col]

        df_cleaned = df[required_cols].copy()

        # Conversion date
        df_cleaned[date_col] = pd.to_datetime(df_cleaned[date_col], errors='coerce')

        # Suppression des lignes avec valeurs manquantes
        df_cleaned = df_cleaned.dropna(subset=required_cols)

        # Tri chronologique
        df_cleaned = df_cleaned.sort_values(by=date_col, ascending=True)

        # Mapping objet
        metriques = self.mapper.map_to_metriques(df_cleaned)

        return metriques
