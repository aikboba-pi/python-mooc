class LotteryNumbers:
    def __init__(self, week_number: int, winning_numbers: list):
        self.week_number = week_number
        self.winning_numbers = winning_numbers

    def number_of_hits(self, numbers: list) -> int:
        return len([n for n in numbers if n in self.winning_numbers])

    def hits_in_place(self, numbers: list) -> list:
        return [n if n in self.winning_numbers else -1 for n in numbers]