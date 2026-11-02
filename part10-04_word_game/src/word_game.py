import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        len1 = len(player1_word)
        len2 = len(player2_word)

        if len1 > len2:
            return 1
        elif len2 > len1:
            return 2
        else:
            return 0  # tie


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouyAEIOUY"
        vowels1 = sum(1 for char in player1_word if char in vowels)
        vowels2 = sum(1 for char in player2_word if char in vowels)

        if vowels1 > vowels2:
            return 1
        elif vowels2 > vowels1:
            return 2
        else:
            return 0  # tie


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = {"rock", "paper", "scissors"}
        p1_valid = player1_word in valid_moves
        p2_valid = player2_word in valid_moves

        # Handling invalid inputs
        if not p1_valid and not p2_valid:
            return 0  # both invalid -> tie
        if not p1_valid:
            return 2  # player 1 invalid -> player 2 wins
        if not p2_valid:
            return 1  # player 2 invalid -> player 1 wins

        # Both inputs are valid
        if player1_word == player2_word:
            return 0  # tie

        # Winning combinations for player 1
        winning_moves = {
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock"),
        }

        if (player1_word, player2_word) in winning_moves:
            return 1
        else:
            return 2