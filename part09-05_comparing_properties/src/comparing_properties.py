# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: "RealProperty") -> bool:
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to: "RealProperty") -> int:
        total_price_self = self.square_metres * self.price_per_sqm
        total_price_compared = compared_to.square_metres * compared_to.price_per_sqm
        return abs(total_price_self - total_price_compared)

    def more_expensive(self, compared_to: "RealProperty") -> bool:
        total_price_self = self.square_metres * self.price_per_sqm
        total_price_compared = compared_to.square_metres * compared_to.price_per_sqm
        return total_price_self > total_price_compared
