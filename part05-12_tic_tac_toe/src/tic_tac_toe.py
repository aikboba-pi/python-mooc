# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    # Validate coordinates
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False
    
    # Check if the square is empty
    if game_board[y][x] != "":
        return False
    
    # Place the piece
    game_board[y][x] = piece
    return True