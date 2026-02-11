"""
Module de décoration pour l'affichage d'une station.
"""
from ui.i_display_decorator import IDisplayDecorator
from ui.metrique_display_decorator import MetriqueDisplayDecorator
from models.station import Station

class StationDisplayDecorator(IDisplayDecorator):
    """
    Décorateur permettant d'afficher les informations d'une station et ses métriques récentes.
    """

    def __init__(self, station: Station):
        """Initialise le décorateur avec la station."""
        self.station = station

    def show(self) -> str:
        """Retourne une chaîne formatée affichant l'en-tête de la station et ses relevés."""
        # Construction de l'en-tête de la station
        lines = []
        lines.append(f"Station : {self.station.nom}")
        lines.append("-" * 60)
        lines.append(f"{'Date':<25} | {'Temp.':>10} | {'Hum.':>8} | {'Pres.':>8}")
        lines.append("-" * 60)

        recent_metriques = (
            self.station.metriques[-10:]
            if len(self.station.metriques) > 10
            else self.station.metriques
        )
        for metrique in recent_metriques:
            decorator = MetriqueDisplayDecorator(metrique)
            lines.append(decorator.show())

        return "\n".join(lines)

# Decorator
