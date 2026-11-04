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
