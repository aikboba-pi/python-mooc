# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    seen = []
    for number in sudoku[row_no]:
        if number != 0:
            if number in seen:
                return False
            seen.append(number)
    return True