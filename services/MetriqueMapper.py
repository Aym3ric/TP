from IDataMapper import IDataMapper
from models.Metrique import Metrique
import pandas as pd
from typing import List

class MetriqueMapper(IDataMapper):    
    DATE_COL = 'heure_utc'
    TEMP_COL = 'temperature'
    HUMID_COL = 'humidite'
    PRESS_COL = 'pression'
    
    def map_to_metriques(self, df: pd.DataFrame) -> List[Metrique]:
        metriques = []
        
        required_cols = [self.DATE_COL, self.TEMP_COL, self.HUMID_COL, self.PRESS_COL]
        if not all(col in df.columns for col in required_cols):
            print(f"Erreur de mapping: Colonnes requises {required_cols} non trouvées.")
            return []

        for index, row in df.iterrows():
            try:
                metrique = Metrique(
                    date=row[self.DATE_COL],
                    temperature=float(row[self.TEMP_COL]),
                    humidite=float(row[self.HUMID_COL]),
                    pression=float(row[self.PRESS_COL])
                )
                metriques.append(metrique)
            except (ValueError, TypeError) as e:
                print(f"Alerte: Ligne ignorée (index {index}), donnée invalide : {e}")

        return metriques