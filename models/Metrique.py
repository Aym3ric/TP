"""
Module définissant le modèle de données Metrique.
"""

class Metrique:
    """
    Classe représentant une mesure météorologique à un instant T.
    """
    def __init__(self, date: str, temperature: float, humidite: int, pression: int) -> None:
        """Initialise une métrique."""
        self.date: str = date
        self.temperature: float = temperature
        self.humidite: int = humidite
        self.pression: int = pression

    def __repr__(self) -> str:
        return (
            f"Metrique(date={self.date}, "
            f"temperature={self.temperature:.1f}°C, "
            f"humidite={self.humidite}%, "
            f"pression={self.pression} Pa)"
        )

class MetriqueBuilder:
    """
    Pattern Builder pour faciliter la création d'objets Metrique.
    """
    def __init__(self):
        self._date = None
        self._temperature = 0.0
        self._humidite = 0
        self._pression = 0

    def with_date(self, date: str):
        """Définit la date."""
        self._date = date
        return self

    def with_temperature(self, temp: float):
        """Définit la température."""
        self._temperature = temp
        return self

    def with_humidite(self, hum: int):
        """Définit l'humidité."""
        self._humidite = hum
        return self

    def with_pression(self, pres: int):
        """Définit la pression."""
        self._pression = pres
        return self

    def build(self) -> Metrique:
        """Construit et retourne l'objet Metrique."""
        return Metrique(self._date, self._temperature, self._humidite, self._pression)

# Builder
