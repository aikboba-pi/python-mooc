# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    seen = set()
    for number in sudoku[row_no]:
        if number != 0:
            if number in seen:
                return False
            seen.add(number)
    return True


def column_correct(sudoku: list, column_no: int) -> bool:
    seen = set()
    for row in sudoku:
        number = row[column_no]
        if number != 0:
            if number in seen:
                return False
            seen.add(number)
    return True


def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    seen = set()
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            number = sudoku[i][j]
            if number != 0:
                if number in seen:
                    return False
                seen.add(number)
    return True


def sudoku_grid_correct(sudoku: list) -> bool:
    # Check all 9 rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    # Check all 9 columns
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False

    # Check all 9 blocks (top-left corners at multiples of 3)
    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            if not block_correct(sudoku, row_no, column_no):
                return False

    return True