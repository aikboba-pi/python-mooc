# Write your solution here
from datetime import date

millennium_eve = date(1999, 12, 31)

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = date(year, month, day)

diff = (millennium_eve - birth_date).days

if diff > 0:
    print(f"You were {diff} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")