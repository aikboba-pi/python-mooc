# write your solution here
def load_matrix():
    """Reads matrix.txt and returns it as a list of lists of integers."""
    matrix = []
    with open("matrix.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                row = [int(val) for val in line.split(",")]
                matrix.append(row)
    return matrix


def matrix_sum():
    """Returns the sum of all elements in matrix.txt."""
    matrix = load_matrix()
    return sum(sum(row) for row in matrix)


def matrix_max():
    """Returns the maximum element in matrix.txt."""
    matrix = load_matrix()
    return max(max(row) for row in matrix)


def row_sums():
    """Returns a list of the sums of each row in matrix.txt."""
    matrix = load_matrix()
    return [sum(row) for row in matrix]