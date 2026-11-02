# Write your solution here
def column_correct(sudoku: list, column_no: int) -> bool:
    seen = set()
    for row in sudoku:
        number = row[column_no]
        if number != 0:
            if number in seen:
                return False
            seen.add(number)
    return True