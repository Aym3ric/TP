from IDisplayDecorator import IDisplayDecorator
from models.Metrique import Metrique

class MetriqueDisplayDecorator(IDisplayDecorator):
    
    def __init__(self, metrique: Metrique):
        self.metrique = metrique 
        
    def show(self) -> str:
        met = self.metrique
        
        date_str = met.date.strftime('%Y-%m-%d %H:%M:%S') if hasattr(met.date, 'strftime') else str(met.date)
        
        return (
            f"{date_str:<25} | "
            f"{met.temperature:>10.1f}°C | "
            f"{met.humidite:>8.0f}% | "
            f"{met.pression:>8.0f} Pa"
        )