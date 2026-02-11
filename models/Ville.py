"""
Module définissant le modèle Ville.
"""
from models.station import Station

class Ville:
    """
    Classe représentant une ville contenant plusieurs stations.
    """
    def __init__(self, nom: str, stations: list[Station] = None) -> None:
        """Initialise une ville."""
        self.nom: str = nom
        self.stations: list[Station] = stations if stations is not None else []

    def add_station(self, station: Station):
        """Ajoute une station à la ville."""
        self.stations.append(station)
