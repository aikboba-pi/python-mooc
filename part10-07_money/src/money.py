class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self) -> str:
        return f"{self.__euros}.{self.__cents:02d} eur"

    def _total_cents(self) -> int:
        return self.__euros * 100 + self.__cents

    def __eq__(self, another: "Money") -> bool:
        return self._total_cents() == another._total_cents()

    def __ne__(self, another: "Money") -> bool:
        return self._total_cents() != another._total_cents()

    def __lt__(self, another: "Money") -> bool:
        return self._total_cents() < another._total_cents()

    def __gt__(self, another: "Money") -> bool:
        return self._total_cents() > another._total_cents()

    def __add__(self, another: "Money") -> "Money":
        total_cents = self._total_cents() + another._total_cents()
        euros = total_cents // 100
        cents = total_cents % 100
        return Money(euros, cents)

    def __sub__(self, another: "Money") -> "Money":
        diff_cents = self._total_cents() - another._total_cents()
        if diff_cents < 0:
            raise ValueError("a negative result is not allowed")
        euros = diff_cents // 100
        cents = diff_cents % 100
        return Money(euros, cents)