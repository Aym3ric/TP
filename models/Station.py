"""
Module définissant le modèle Station.
"""
from typing import List
from models.metrique import Metrique

class Station:
    """
    Classe représentant une station météorologique et ses relevés.
    """
    def __init__(self, nom: str) -> None:
        """Initialise une station avec un nom."""
        self.nom: str = nom
        self.metriques: List[Metrique] = []

    def add_metrique(self, metrique: Metrique) -> None:
        """Ajoute une métrique à la station."""
        self.metriques.append(metrique)
