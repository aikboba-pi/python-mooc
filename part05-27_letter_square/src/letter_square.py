# Write your solution here
import string

layers = int(input("Layers: "))
alphabet = string.ascii_uppercase

size = 2 * layers - 1

for r in range(size):
    row_chars = []
    for c in range(size):
        # Distance from the edge of the square
        dist_from_edge = min(r, c, size - 1 - r, size - 1 - c)
        
        # Determine the corresponding character
        char_index = layers - 1 - dist_from_edge
        row_chars.append(alphabet[char_index])
        
    print("".join(row_chars))