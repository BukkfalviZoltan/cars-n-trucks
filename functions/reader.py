import csv
import json
# 1. feladat:
# Készíts egy functiont, ami paraméterként megkap egy .txt file elérési útját.
# A function olvassa be a file teljes tartalmát.
#
# A file minden sora egy truck adatait tartalmazza ilyen formában:
# type|brand|model|year|color
#
# Alakítsd át minden sort egy dictionaryvé, majd ezeket tedd bele egy listába.
#
# A function a végén térjen vissza egy listányi dictionaryvel.
#
# Példa egy dictionaryre:
# {
#     "type": "truck",
#     "brand": "Volvo",
#     "model": "FH16",
#     "year": 2020,
#     "color": "red"
# }


def read_trucks(file_path):
    trucks = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")

            truck = {
                "type": data[0],
                "brand": data[1],
                "model": data[2],
                "year": int(data[3]),
                "color": data[4],
            }

            trucks.append(truck)

    return trucks


# 2. feladat:
# Készíts egy functiont, ami paraméterként megkap egy .json file elérési útját.
# A function olvassa be a JSON file tartalmát.
#
# A JSON file több car adatait tartalmazza.
#
# A function a végén térjen vissza ugyanúgy egy listányi dictionaryvel.
#
# Példa:
# [
#     {
#         "type": "car",
#         "brand": "Toyota",
#         "model": "Corolla",
#         "year": 2021,
#         "color": "white"
#     }
# ]
def read_cars(file_path):
    cars = []

    with open(file_path, "r", encoding="utf-8") as f:
        cars = json.load(f)

    return cars


# 3. feladat:
# Készíts egy functiont, ami paraméterként megkapja
# a trucks listát és a cars listát.
#
# A function egyesítse a két listát egyetlen listává.
#
# Fontos, hogy az egyesített lista elemei dictionaryk legyenek,
# azonos kulcsokkal, hogy később csv.DictWriter segítségével
# ki tudjuk írni őket egy CSV fileba.
#
# Minden dictionary ilyen kulcsokat tartalmazzon:
# type
# brand
# model
# year
# color
#
# A function a végén térjen vissza az egyesített listával.


def merge_vehicles(trucks, cars):
    vehicles = trucks + cars

    return vehicles


# 4. feladat:
# Készíts egy functiont, ami paraméterként megkapja
# a 3. feladatból visszakapott egyesített vehicles listát
# és a vehicles.csv file elérési útját.
#
# Mielőtt kiírnád az adatokat a CSV fileba,
# rendezd a járműveket year alapján csökkenő sorrendbe,
# vagyis a legújabb járművek legyenek elöl.
#
# Ezután csv.DictWriter segítségével írd bele az adatokat
# a vehicles.csv fileba.
#
# A CSV file tartalmazzon headert is:
# type,brand,model,year,color
#
# A végeredményben tehát a legújabb autók és truckok
# szerepeljenek legfelül, majd haladjanak a régebbiek felé.
def get_year(vehicle):
    return vehicle["year"]


def save_vehicles(vehicles, file_path):
    sorted_vehicles = sorted(vehicles, key=get_year, reverse=True)

    with open(file_path, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["type", "brand", "model", "year", "color"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(sorted_vehicles)
