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
