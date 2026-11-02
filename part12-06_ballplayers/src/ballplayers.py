class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


def most_goals(players: list[BallPlayer]) -> str:
    top_scorer = max(players, key=lambda player: player.goals)
    return top_scorer.name


def most_points(players: list[BallPlayer]) -> tuple[str, int]:
    best_player = max(players, key=lambda player: player.goals + player.passes)
    return (best_player.name, best_player.number)


def least_minutes(players: list[BallPlayer]) -> BallPlayer:
    return min(players, key=lambda player: player.minutes)