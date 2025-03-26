from datetime import date

class Game:
    def __init__(self, gameId: int, title: str, genre: str, releaseDate: date, rating: float):
        self.gameId = gameId
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.rating = rating
        self.suggestions = suggestions
