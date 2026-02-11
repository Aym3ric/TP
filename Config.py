"""
Module de configuration de l'application.
"""

class Configuration:
    """
    Classe Singleton gérant la configuration globale de l'application.
    """
    instance = None

    def __new__(cls):
        """Crée ou retourne l'instance unique de Configuration."""
        if cls.instance is None:
            cls.instance = super(Configuration, cls).__new__(cls)

            cls.instance.config = {
                "Compans Cafarelli": {
                    "csv": "data/compans cafarelli.csv",
                    "api": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/42-station-meteo-toulouse-parc-compans-cafarelli/exports/csv?lang=fr&timezone=UTC&use_labels=false&delimiter=%3B"
                },
                "Carmes": {
                    "csv": "data/carmes.csv",
                    "api": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/28-station-meteo-toulouse-carmes/exports/csv?lang=fr&timezone=UTC&use_labels=false&delimiter=%3B"
                }
            }
        return cls.instance

    def get_all(self):
        """Retourne la configuration complète."""
        return self.config

# Singleton
