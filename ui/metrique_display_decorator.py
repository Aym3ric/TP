"""
Module de décoration pour l'affichage d'une métrique.
"""
from ui.i_display_decorator import IDisplayDecorator
from models.metrique import Metrique

class MetriqueDisplayDecorator(IDisplayDecorator):
    """
    Décorateur permettant d'afficher une métrique formatée.
    """

    def __init__(self, metrique: Metrique):
        """Initialise le décorateur avec la métrique à afficher."""
        self.metrique = metrique

    def show(self) -> str:
        """Retourne une chaîne formatée représentant la métrique."""
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
