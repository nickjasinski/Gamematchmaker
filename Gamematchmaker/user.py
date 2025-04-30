from typing import List, Optional
from game import Game
from preferences import Preferences
from review import Review
from suggestion import Suggestion
from user_profile import Profile
from wishlist import Wishlist


class User:
    def __init__(self,
                 userID: Optional[int],
                 username: str,
                 email: str,
                 password: str,
                 profile: Optional[Profile] = None,
                 wishlist: Optional[str] = None,
                 friends: Optional[List['User']] = None,
                 blocked: Optional[List['User']] = None):
        self.userID = userID
        self.username = username
        self.email = email
        self.password = password
        self.profile = profile
        self.wishlist = wishlist if wishlist else Wishlist()
        self.friends = friends if friends else []
        self.blocked = blocked if blocked else []

    def signUp(self, username: str, email: str, password: str) -> bool:
        # Placeholder logic
        self.username = username
        self.email = email
        self.password = password
        return True

    def logIn(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password

    def logOut(self):
        print(f"User {self.username} logged out.")

    def createProfile(self, name: str, favoriteGame: Game, bio: str):
        self.profile = Profile(
            name=name, favorite_game=favoriteGame.name, bio=bio, user=self)

    def addFriend(self, friend: 'User') -> bool:
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        return False

    def removeFriend(self, friend: 'User') -> bool:
        if friend in self.friends:
            self.friends.remove(friend)
            return True
        return False

    def blockUser(self, user: 'User') -> bool:
        if user not in self.blocked:
            self.blocked.append(user)
            return True
        return False

    def addToWishlist(self, game: Game) -> bool:
        return self.wishlist.addGame(game)

    def removeFromWishlist(self, game: Game) -> bool:
        return self.wishlist.removeGame(game)

    def writeReview(self, game: Game, content: str, rating: int) -> Review:
        return Review(
            reviewId = None,      
            userID = self.userID,
            gameID = game.gameID,       
            content = content,
            rating = rating
    )

    def likeReview(self, review: Review):
        review.like()

    def dislikeReview(self, review: Review):
        review.dislike()

    def addSuggestion(self, game: Game, content: str) -> Suggestion:
        return Suggestion(game=game, user=self, content=content)

    def managePreferences(self, preferences: Preferences):
        self.preferences = preferences
