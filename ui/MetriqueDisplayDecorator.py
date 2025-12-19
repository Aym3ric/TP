from ui.IDisplayDecorator import IDisplayDecorator
from models.Metrique import Metrique

class MetriqueDisplayDecorator(IDisplayDecorator):
    
    def __init__(self, metrique: Metrique):
        self.metrique = metrique 
        
    def show(self) -> str:
        met = self.metrique
        
        if hasattr(met.date, 'strftime'):
            date_str = met.date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            date_str = str(met.date)
        
        return (
            f"{date_str:<25} | "
            f"{met.temperature:>8.1f}°C | "
            f"{met.humidite:>7.0f}% | "
            f"{met.pression:>6.0f} Pa"
        )

# Decorator