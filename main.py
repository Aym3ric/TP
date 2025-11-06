""" import pandas as pd 
from station import Station
from ville import Ville
from metrique import Metrique
from ExtractCsv import ExtractCsv

df = pd.read_csv('42-station-meteo-toulouse-parc-compans-cafarelli.csv', delimiter=';')
extract_csv = ExtractCsv()
station_compans_cafarelli = Station('Compans Cafarelli')
#print(df.head())

for indice in range(df):
    date = df['heure_utc']
    temperature = df['temperature']
    humidite = df['humidite']
    pression = df['pression']
    metrique_station = Metrique(date, temperature, humidite, pression)
    break
    station_compans_cafarelli.metrique.append(metrique_station)

#print(station_compans_cafarelli.metrique[0].date)
toulouse = Ville("Toulouse", station_compans_cafarelli)
#station_compans_cafarelli.show()
 """

from Application import Application
from ExtractCsv import ExtractCsv

extractor = ExtractCsv("42-station-meteo-toulouse-parc-compans-cafarelli.csv")
Application(extractor).run()