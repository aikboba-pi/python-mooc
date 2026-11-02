class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return f"{self.__day}.{self.__month}.{self.__year}"

    def _to_days(self) -> int:
        return self.__year * 360 + (self.__month - 1) * 30 + self.__day

    @classmethod
    def _from_days(cls, total_days: int) -> "SimpleDate":
        year = total_days // 360
        remainder = total_days % 360
        
        if remainder == 0:
            year -= 1
            month = 12
            day = 30
        else:
            month = (remainder - 1) // 30 + 1
            day = (remainder - 1) % 30 + 1
            
        return cls(day, month, year)

    def __eq__(self, another: "SimpleDate") -> bool:
        return self._to_days() == another._to_days()

    def __ne__(self, another: "SimpleDate") -> bool:
        return self._to_days() != another._to_days()

    def __lt__(self, another: "SimpleDate") -> bool:
        return self._to_days() < another._to_days()

    def __gt__(self, another: "SimpleDate") -> bool:
        return self._to_days() > another._to_days()

    def __add__(self, days: int) -> "SimpleDate":
        total_days = self._to_days() + days
        return SimpleDate._from_days(total_days)

    def __sub__(self, another: "SimpleDate") -> int:
        return abs(self._to_days() - another._to_days())