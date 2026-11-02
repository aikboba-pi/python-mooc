# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self) -> int:
        return self.numbers

    def get_sum(self) -> int:
        return self.total_sum

    def average(self) -> float:
        if self.numbers == 0:
            return 0.0
        return self.total_sum / self.numbers


all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

print("Please type in integer numbers:")
while True:
    num = int(input())
    if num == -1:
        break

    all_stats.add_number(num)
    if num % 2 == 0:
        even_stats.add_number(num)
    else:
        odd_stats.add_number(num)

print(f"Sum of numbers: {all_stats.get_sum()}")
print(f"Mean of numbers: {all_stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")