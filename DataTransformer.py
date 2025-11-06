import pandas as pd
from IDataTransformer import IDataTransformer
from Metrique import Metrique
from typing import List

class DataTransformer(IDataTransformer):
    
    def transform(self, df: pd.DataFrame) -> List[Metrique]:
        DATE_COL = 'heure_utc'
        TEMP_COL = 'temperature'
        HUMID_COL = 'humidite'
        PRESS_COL = 'pression'

        required_cols = [DATE_COL, TEMP_COL, HUMID_COL, PRESS_COL]
        if not all(col in df.columns for col in required_cols):
            print(f"Colonnes manquantes. {required_cols} sont requises.")
            print(f"Colonnes trouvées: {list(df.columns)}")
            return []

        df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors='coerce')
        df = df.dropna(subset=[DATE_COL])
        df = df.sort_values(by=DATE_COL, ascending=True)

        metriques = []
        for index, row in df.iterrows():
            try:
                metrique = Metrique(
                    date=row[DATE_COL],
                    temperature=float(row[TEMP_COL]),
                    humidite=float(row[HUMID_COL]),
                    pression=float(row[PRESS_COL])
                )
                metriques.append(metrique)
            except ValueError as e:
                print(f"Alerte: Ligne ignorée, donnée invalide : {e}")

        return metriques