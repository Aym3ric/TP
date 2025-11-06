from IDataTransformer import IDataTransformer
import pandas as pd
from typing import List
from Metrique import Metrique

class DataTransformer(IDataTransformer):
    def transform(self, df: pd.DataFrame) -> list:
        df['heure_de_paris'] = pd.to_datetime(df['heure_de_paris'], errors='coerce')

        df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
        df['humidite'] = pd.to_numeric(df['humidite'], errors='coerce')
        df['pression'] = pd.to_numeric(df['pression'], errors='coerce')

        df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
        df['humidite'] = df['humidite'].fillna(df['humidite'].mean()).astype(int)
        df['pression'] = df['pression'].fillna(df['pression'].mean()).astype(int)

        # Création des objets Metrique
        metriques = [
            Metrique(
                date=row['heure_de_paris'].isoformat(),
                temperature=row['temperature'],
                humidite=int(row['humidite']),
                pression=int(row['pression'])
            )
            for _, row in df.iterrows()
        ]

        return metriques
