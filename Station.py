from Metrique import Metrique 
from typing import List

class Station:
    def __init__(self, id_station: int, nom: str) -> None:
        self.id: int = id_station
        self.nom: str = nom
        self.metriques: List[Metrique] = []

    def ajouter_metrique(self, metrique: Metrique) -> None:
        self.metriques.append(metrique)

    