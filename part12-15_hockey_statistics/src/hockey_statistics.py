import json

class Player:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.assists = data["assists"]
        self.goals = data["goals"]
        self.penalties = data["penalties"]
        self.team = data["team"]
        self.games = data["games"]

    @property
    def points(self) -> int:
        return self.goals + self.assists

    def __str__(self) -> str:
        # Field widths align exactly with the template spec:
        # name: 20 chars left-aligned, followed by 1 space -> team starts at char 22 (index 21)
        # goals: 3 chars right-aligned, '+' at char 30 (index 29)
        # assists: 3 chars right-aligned, '=' at char 35 (index 34)
        # points: 3 chars right-aligned
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.points:3}"

class NHLStatisticsApp:
    def __init__(self):
        self.players = []

    def load_data(self, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.players = [Player(p) for p in data]
        print(f"read the data of {len(self.players)} players")

    def search_player(self):
        name = input("name: ")
        for player in self.players:
            if player.name == name:
                print(player)
                return

    def list_teams(self):
        teams = sorted(set(player.team for player in self.players))
        for team in teams:
            print(team)

    def list_countries(self):
        countries = sorted(set(player.nationality for player in self.players))
        for country in countries:
            print(country)

    def players_in_team(self):
        team = input("team: ")
        team_players = [p for p in self.players if p.team == team]
        team_players.sort(key=lambda p: p.points, reverse=True)
        for player in team_players:
            print(player)

    def players_from_country(self):
        country = input("country: ")
        country_players = [p for p in self.players if p.nationality == country]
        country_players.sort(key=lambda p: p.points, reverse=True)
        for player in country_players:
            print(player)

    def most_points(self):
        how_many = int(input("how many: "))
        # Primary key: points (descending), tie-breaker: goals (descending)
        ranked = sorted(self.players, key=lambda p: (p.points, p.goals), reverse=True)
        for player in ranked[:how_many]:
            print(player)

    def most_goals(self):
        how_many = int(input("how many: "))
        # Primary key: goals (descending), tie-breaker: games played (ascending)
        ranked = sorted(self.players, key=lambda p: (-p.goals, p.games))
        for player in ranked[:how_many]:
            print(player)

    def run(self):
        filename = input("file name: ")
        self.load_data(filename)
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.list_teams()
            elif command == "3":
                self.list_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()

def main():
    app = NHLStatisticsApp()
    app.run()

main()