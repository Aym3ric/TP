from IDisplayDecorator import IDisplayDecorator
from models.Station import Station

class StationDisplayDecorator(IDisplayDecorator):
    
    def __init__(self, station: Station):
        self.station = station 
        
    def show(self) -> str:
        return self.station.nom