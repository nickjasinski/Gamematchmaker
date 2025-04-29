from typing import Optional

class Review:
    def __init__(self, reviewId: Optional[int], userID: int, gameID: int, content: str, rating: int):
        self.reviewId = reviewId
        self.userID = userID
        self.gameID = gameID
        self.content = content
        self.rating = rating
    def like(self):
        pass

    def dislike(self):
        pass