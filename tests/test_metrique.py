"""
Tests unitaires pour la classe Metrique et MetriqueBuilder avec pytest.
"""
from models.metrique import MetriqueBuilder

class TestMetrique:
    """Tests pour la classe Metrique et son Builder."""

    def test_builder(self):
        """Test de la création via Builder."""
        metrique = MetriqueBuilder()\
            .with_date("2024-01-01")\
            .with_temperature(20.5)\
            .with_humidite(50)\
            .with_pression(1013)\
            .build()

        assert metrique.date == "2024-01-01"
        assert metrique.temperature == 20.5
        assert metrique.humidite == 50
        assert metrique.pression == 1013
