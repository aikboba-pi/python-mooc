# write your solution here
import csv

def read_fruits():
    with open("fruits.csv") as my_file:
        reader = csv.reader(my_file, delimiter=";")
        return {col[0]: float(col[1]) for col in reader}