import pandas as pd
from services import IDataMapper
from services.IDataTransformer import IDataTransformer
from models.Metrique import Metrique
from typing import List

class DataTransformer(IDataTransformer):
    
    def __init__(self, mapper: IDataMapper):
        self.mapper = mapper

    def transform(self, df: pd.DataFrame) -> List[Metrique]:
        DATE_COL = 'heure_utc'
        TEMP_COL = 'temperature'
        HUMID_COL = 'humidite'
        PRESS_COL = 'pression'

        required_cols = [DATE_COL, TEMP_COL, HUMID_COL, PRESS_COL]
        
        df_cleaned = df[required_cols].copy() 
        df_cleaned[DATE_COL] = pd.to_datetime(df_cleaned[DATE_COL], errors='coerce')
        df_cleaned = df_cleaned.dropna(subset=[DATE_COL, TEMP_COL, HUMID_COL, PRESS_COL])
        df_cleaned = df_cleaned.sort_values(by=DATE_COL, ascending=True)
        metriques = self.mapper.map_to_metriques(df_cleaned)

        return metriques