# Write your solution here
def row_sums(my_matrix: list[list]):
    for line in my_matrix:
        line.append(sum(line))