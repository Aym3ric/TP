from Application import Application
from Ville import Ville
from Station import Station
from typing import List
from Visualizer import Visualizer
from DataTransformer import DataTransformer
from MetriqueMapper import MetriqueMapper
from IDataMapper import IDataMapper

def setup_data() -> List[Ville]:
    toulouse = Ville("Toulouse")
    station_compans = Station("compans cafarelli") 
    toulouse.add_station(station_compans)
    villes = [toulouse]
    
    return villes

if __name__ == "__main__":
    metrique_mapper: IDataMapper = MetriqueMapper()
    transformer = DataTransformer(mapper=metrique_mapper)
    visualizer = Visualizer()
    villes_config = setup_data()

    app = Application(
        transformer=transformer,
        visualizer=visualizer,
        villes=villes_config
    )

    app.run()