from Metrique import Metrique
import pandas as pd
from typing import List

class IDataTransformer:
    def transform(self, df: pd.DataFrame) -> List[Metrique]:
        pass