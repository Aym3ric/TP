

from application import Application
from services.data_transformer import DataTransformer
from ui.visualizer import Visualizer
from config import Configuration
from services.metrique_mapper import MetriqueMapper

if __name__ == "__main__":
    mapper = MetriqueMapper()
    transformer = DataTransformer(mapper)
    visualizer = Visualizer()

    # Récupération de la configuration via le Singleton
    config = Configuration().get_all()
    app = Application(transformer, visualizer, config)

    app.run()
