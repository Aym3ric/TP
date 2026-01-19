class Configuration:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Configuration, cls).__new__(cls)

            cls.instance.config = {
                "Compans Cafarelli": "data/compans cafarelli.csv",
                "St-Exupery": "data/st-exupery.csv"
            }
        return cls.instance

    def get_all(self):
        return self.config
    
# Singleton 