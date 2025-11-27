from abc import ABC, abstractmethod
import pandas as pd

class IDataExtractor(ABC):
    
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass