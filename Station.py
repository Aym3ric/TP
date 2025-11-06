from Metrique import Metrique 
from typing import List

class Station:
    def __init__(self, nom: str) -> None:
        self.nom: str = nom
        self.metriques: List[Metrique] = []

    def add_metrique(self, metrique: Metrique) -> None:
        self.metriques.append(metrique)

    