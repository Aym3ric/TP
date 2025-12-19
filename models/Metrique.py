class Metrique:
    def __init__(self, date: str, temperature: float, humidite: int, pression: int) -> None:
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
    def __init__(self):
        self._date = None
        self._temperature = 0.0
        self._humidite = 0
        self._pression = 0

    def with_date(self, date: str):
        self._date = date
        return self

    def with_temperature(self, temp: float):
        self._temperature = temp
        return self

    def with_humidite(self, hum: int):
        self._humidite = hum
        return self

    def with_pression(self, pres: int):
        self._pression = pres
        return self

    def build(self) -> Metrique:
        return Metrique(self._date, self._temperature, self._humidite, self._pression)
    
# Builder