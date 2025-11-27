from abc import ABC, abstractmethod
from models.Metrique import Metrique
import pandas as pd
from typing import List

class IDataMapper(ABC):
    
    @abstractmethod
    def map_to_metriques(self, df: pd.DataFrame) -> List[Metrique]:
        pass