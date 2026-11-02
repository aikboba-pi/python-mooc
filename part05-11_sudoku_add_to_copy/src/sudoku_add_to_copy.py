# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    # Create a deep copy of the sudoku grid (copy each inner row separately)
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])   # row[:] creates a shallow copy of the row
    
    # Add the number to the copy
    new_sudoku[row_no][column_no] = number
    
    return new_sudoku