from Metrique import Metrique 
from typing import List
from Ville import Ville
from Station import Station
from MetriqueDisplayDecorator import MetriqueDisplayDecorator
from StationDisplayDecorator import StationDisplayDecorator

class Visualizer:
    def __init__(self):
        pass

    def choice_type_extract(self) -> str:
        print("-> CSV")
        while True:
            response = input("Type d'extraction : ").lower()
            if response == 'csv':
                 return response

    def choice_ville(self, villes: List[Ville]) -> Ville:
        available_names = {v.nom.lower(): v for v in villes}
        
        print(f"Villes disponibles: {', '.join([v.nom for v in villes])}")
        
        while True:
            response = input("Ville : ").lower()
            if response in available_names:
                 return available_names[response]
            print(f"Ville invalide. Veuillez choisir parmi : {', '.join([v.nom for v in villes])}")

    def choice_station(self, ville: Ville) -> Station:
        available_names = {s.nom.lower(): s for s in ville.stations}
        
        station_names = [StationDisplayDecorator(s).show() for s in ville.stations]
        print(f"Stations disponibles pour {ville.nom}: {', '.join(station_names)}")

        while True:
            response = input("Station : ").lower()
            if response in available_names:
                return available_names[response]
            print(f"Station invalide. Veuillez choisir parmi : {', '.join(station_names)}")

    def show_history(self, history: List[Metrique]):
        print(f"{'Date':<25} | {'Température':>12} | {'Humidité':>9} | {'Pression':>8}")
        
        for metrique_data in history[-10:]:
            displayable_metrique = MetriqueDisplayDecorator(metrique_data)
            print(displayable_metrique.show())

    def ask_for_refresh(self) -> bool:
        print("-" * 40)
        while True:
            response = input("Voulez-vous rafraîchir les données ? (o/n) : ").lower().strip()
            if response == 'o':
                return True
            if response == 'n':
                return False
            print("Réponse invalide. Veuillez entrer 'o' pour oui ou 'n' pour non.")