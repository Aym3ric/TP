from ui.IDisplayDecorator import IDisplayDecorator
from models.Station import Station
from ui.MetriqueDisplayDecorator import MetriqueDisplayDecorator

class StationDisplayDecorator(IDisplayDecorator):
    
    def __init__(self, station: Station):
        self.station = station 
        
    def show(self) -> str:
        # Construction de l'en-tête de la station
        lines = []
        lines.append(f"Station : {self.station.nom}")
        lines.append("-" * 60)
        lines.append(f"{'Date':<25} | {'Temp.':>10} | {'Hum.':>8} | {'Pres.':>8}")
        lines.append("-" * 60)
        
        # Itération sur les métriques et délégation de l'affichage
        for metrique in self.station.metriques:
            decorator = MetriqueDisplayDecorator(metrique)
            lines.append(decorator.show())
            
        return "\n".join(lines)

# Decorator