from typing import Optional

class Review:
    def __init__(self, reviewId: Optional[int], userID: int, gameID: int, content: str, rating: int, likes: int = 0, dislikes: int = 0):
        self.reviewId = reviewId
        self.userID = userID
        self.gameID = gameID
        self.content = content
        self.rating = rating
        self.likes = likes
        self.dislikes = dislikes

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1