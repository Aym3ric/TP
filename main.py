from Application import Application
from services.DataTransformer import DataTransformer
from ui.Visualizer import Visualizer
from Config import STATIONS_CONFIG

if __name__ == "__main__":
    transformer = DataTransformer()
    visualizer = Visualizer()

    app = Application(transformer, visualizer, STATIONS_CONFIG)
    app.run()