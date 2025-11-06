from Station import Station

class Ville:
    def __init__(self, nom: str, stations: list[Station] = []) -> None:
        self.nom: str = nom
        self.stations: list[Station] = stations

    def add_station(self, station: Station):
        self.stations.append(station)
