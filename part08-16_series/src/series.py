# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def __str__(self) -> str:
        genres_str = ", ".join(self.genres)
        info = f"{self.title} ({self.seasons} seasons)\ngenres: {genres_str}\n"

        if len(self.ratings) == 0:
            info += "no ratings"
        else:
            avg = sum(self.ratings) / len(self.ratings)
            info += f"{len(self.ratings)} ratings, average {avg:.1f} points"

        return info


def minimum_grade(rating: float, series_list: list) -> list:
    result = []
    for series in series_list:
        if len(series.ratings) > 0:
            avg = sum(series.ratings) / len(series.ratings)
            if avg >= rating:
                result.append(series)
    return result


def includes_genre(genre: str, series_list: list) -> list:
    return [series for series in series_list if genre in series.genres]