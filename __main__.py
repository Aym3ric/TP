import sys
import os

from Application import Application
from services.DataTransformer import DataTransformer
from ui.Visualizer import Visualizer
from Config import Configuration
from services.MetriqueMapper import MetriqueMapper

if __name__ == "__main__":
    mapper = MetriqueMapper()
    transformer = DataTransformer(mapper)
    visualizer = Visualizer()

    # Récupération de la configuration via le Singleton
    config = Configuration().get_all()
    app = Application(transformer, visualizer, config)
    
    app.run()