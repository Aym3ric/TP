# Data Profiling — Jeu de données météo Toulouse

## Source des données

Les données proviennent de l'**Open Data Toulouse Métropole** :
- [Station Compans Cafarelli](https://data.toulouse-metropole.fr/explore/dataset/42-station-meteo-toulouse-parc-compans-cafarelli/)
- [Station Carmes](https://data.toulouse-metropole.fr/explore/dataset/28-station-meteo-toulouse-carmes/)

Deux modes d'accès : fichiers **CSV** locaux (delimiter `;`) et **API REST** (format JSON).

---

## Structure des données

Chaque fichier/réponse API contient **15 colonnes** identiques pour les deux stations :

| Colonne | Type | Description |
|---|---|---|
| `heure_utc` | datetime | Horodatage UTC du relevé (toutes les 15 min) |
| `heure_de_paris` | datetime | Horodatage heure de Paris |
| `temperature` | float | Température en °C |
| `humidite` | float | Humidité relative en % |
| `pression` | float | Pression atmosphérique en Pa |
| `pluie` | float | Précipitations (mm) |
| `pluie_intensite_max` | float | Intensité max de pluie |
| `force_moyenne_du_vecteur_vent` | float | Vitesse moyenne du vent |
| `force_rafale_max` | float | Vitesse max des rafales |
| `direction_du_vecteur_vent_moyen` | float | Direction moyenne du vent (°) |
| `direction_du_vecteur_de_vent_max` | float | Direction du vent max (°) |
| `direction_du_vecteur_de_rafale_de_vent_max` | float | Direction de la rafale max (°) |
| `type_de_station` | string | Type de la station météo |
| `id` | float | Identifiant du relevé |
| `data` | string | Identifiant du relevé |

> **Note** : L'application n'utilise que 4 colonnes : `heure_utc`, `temperature`, `humidite`, `pression`.

Fréquence d'échantillonnage : **1 relevé toutes les 15 minutes**.

---

## Statistiques des colonnes utilisées

### Compans Cafarelli

| Métrique | Température (°C) | Humidité (%) | Pression (Pa) |
|---|---|---|---|
| Min | -50.0 | 0 | 90 000 |
| Max | 42.6 | 97 | 102 500 |
| Moyenne | 14.96 | 64.80 | 99 943 |

### Carmes

| Métrique | Température (°C) | Humidité (%) | Pression (Pa) |
|---|---|---|---|
| Min | -50.0 | 0 | 90 000 |
| Max | 40.5 | 97 | 102 400 |
| Moyenne | 12.98 | 70.64 | 99 428 |

---

## Qualité des données

- **Valeurs manquantes** : 20 lignes (~0.01%) pour Compans Cafarelli, 39 lignes (~0.03%) pour Carmes — traitées par suppression via `dropna()` dans le `DataTransformer`.
- **Valeurs aberrantes** : Les températures minimales de **-50°C** sont probablement des erreurs de capteur. La pression minimale de **90 000 Pa** est également suspecte.
- **Nettoyage appliqué** : conversion des dates, suppression des lignes incomplètes, tri chronologique.

---

## API

L'API retourne les mêmes colonnes au format JSON. Par défaut, l'application récupère les **10 derniers relevés** triés par `heure_utc` décroissant.
