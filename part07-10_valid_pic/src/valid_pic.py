# Write your solution here
from datetime import date

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    century_marker = pic[6]
    century_map = {
        "+": 1800,
        "-": 1900,
        "A": 2000
    }

    if century_marker not in century_map:
        return False

    day_str = pic[0:2]
    month_str = pic[2:4]
    year_str = pic[4:6]
    yyy_str = pic[7:10]
    control_char = pic[10]

    if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit() and yyy_str.isdigit()):
        return False

    full_year = century_map[century_marker] + int(year_str)
    try:
        date(full_year, int(month_str), int(day_str))
    except ValueError:
        return False

    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit_number = int(pic[0:6] + yyy_str)
    remainder = nine_digit_number % 31

    expected_control_char = control_string[remainder]

    return control_char == expected_control_char