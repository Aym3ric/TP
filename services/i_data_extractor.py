from abc import ABC, abstractmethod
import pandas as pd

class IDataExtractor(ABC):
    """
    Interface Command pour l'extraction de données.
    """
    @abstractmethod
    def execute(self) -> pd.DataFrame:
        pass

# Command
