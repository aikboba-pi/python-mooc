# Write your solution here
def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        # Add a blank line before every 3rd row (except the first)
        if i > 0 and i % 3 == 0:
            print()
        
        line = ""
        for j, number in enumerate(row):
            # Add a space before every 3rd column (except the first)
            if j > 0 and j % 3 == 0:
                line += " "
            
            if number == 0:
                line += "_ "
            else:
                line += f"{number} "
        
        print(line)


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number