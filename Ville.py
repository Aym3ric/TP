from Station import Station

class Ville:
    def __init__(self, nom: str) -> None:
        self.nom: str = nom
        self.stations: list[Station] = []

    def add_station(self, station: Station):
        self.stations.append(station)
