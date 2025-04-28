from datetime import date
from typing import List, Optional

class Game:
    """Constructor for a video game"""
    def __init__(
        self, 
        gameID: int,
        name: str,
        genres: List[str],
        platforms: List[str],
        release_date: Optional[date],
        rating: Optional[float],
        summary: Optional[str]
    ):
        self.name = name
        self.gameID = gameID
        self.genres = genres
        self.platforms = platforms
        self.release_date = release_date
        self.rating = rating
        self.summary = summary

    """String representation of the Game object"""
    def __str__(self):
        return (
            f"Title: {self.name or 'N/A'}\n"
            f"Genres: {', '.join(self.genres) if self.genres else 'N/A'}\n"
            f"Platforms: {', '.join(self.platforms) if self.platforms else 'N/A'}\n"
            f"Release Date: {self.release_date or 'N/A'}\n"
            f"Rating: {f'{self.rating:.1f}' if self.rating is not None else 'N/A'}\n"
            f"Summary: {self.summary or 'N/A'}"
        )