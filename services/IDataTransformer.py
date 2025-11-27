from abc import ABC, abstractmethod
from models.Metrique import Metrique
import pandas as pd
from typing import List

class IDataTransformer(ABC):
    
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> List[Metrique]:
        pass