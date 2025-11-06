from Metrique import Metrique 
from typing import List

class Visualizer:
    def __init__(self):
        pass

    def choice_type_extract():
        print("-> CSV")
        while True:
            response = input("Type d'extraction : ").lower()

            if response == 'csv':
                 return response

    def choice_ville():
        print("-> Toulouse")
        while True:
            response = input("Ville : ").lower()

            if response == 'toulouse':
                 return response

    def choice_station(self, ville: str):
        if ville == 'toulouse':
            print("-> Compans Cafarelli")
            while True:
                response = input("Station : ").lower()

                if response == 'compans cafarelli':
                    return response

    def show_history(self, history: List[Metrique]):
        print(f"{'Date':<28} | {'Température':>12} | {'Humidité':>9} | {'Pression':>8}")

        for hist in history[-10:]:
            print(f"{hist.date:<28} | {hist.temperature:>10.1f}°C | {hist.humidite:>8}% | {hist.pression:>8} Pa")

