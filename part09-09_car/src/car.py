class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        if km <= 0:
            return

        # The car can only drive as far as the available petrol allows
        actual_distance = min(km, self.__petrol)
        self.__odometer += actual_distance
        self.__petrol -= actual_distance

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"