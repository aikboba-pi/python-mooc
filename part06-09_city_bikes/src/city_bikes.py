# tee ratkaisu tänne
# Write your solution here
import math
from itertools import combinations


def get_station_data(filename: str):
    stations = {}

    with open(filename, encoding="utf-8") as file:
        # Skip the header line
        next(file)

        for line in file:
            parts = line.strip().split(";")

            longitude = float(parts[0])
            latitude = float(parts[1])
            name = parts[3]

            stations[name] = (longitude, latitude)

    return stations


def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2

    return math.sqrt(x_km ** 2 + y_km ** 2)


def greatest_distance(stations: dict):
    greatest = 0
    station_a = None
    station_b = None

    for name1, name2 in combinations(stations, 2):
        current_distance = distance(stations, name1, name2)

        if current_distance > greatest:
            greatest = current_distance
            station_a = name1
            station_b = name2

    return station_a, station_b, greatest