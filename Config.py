class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            # Initialisation de la configuration unique
            cls._instance._config = {
                "Compans Cafarelli": "data/compans cafarelli.csv",
                "Jardin des Plantes": "data/jardin_plantes.csv",
                "Marengo SNCF": "data/marengo.csv"
            }
        return cls._instance

    def get(self, key):
        return self._config.get(key)

    def get_all(self):
        return self._config
    
# Singleton 