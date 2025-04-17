from typing import List
from game import Game
from profile import Profile
from wishlist import Wishlist
from preferences import Preferences
from review import Review
from suggestion import Suggestion


class User:
    def __init__(self, userID: int, username: str, email: str, password: str, profile: Profile = None, wishlist: Wishlist = None, friends: List['User'] = None, blocked: List['User'] = None):
        self.userID = userID
        self.username = username
        self.email = email
        self.password = password
        self.profile = profile
        self.wishlist = wishlist
        self.friends = friends
        self.blocked = blocked

    def signUp(self, username: str, email: str, password: str) -> bool:
        pass

    def logIn(self, email: str, password: str) -> bool:
        pass

    def logOut(self):
        pass

    def createProfile(self, name: str, favoriteGame: Game, bio: str):
        pass

    def addFriend(self, friend: 'User') -> bool:
        pass

    def removeFriend(self, friend: 'User') -> bool:
        pass

    def blockUser(self, user: 'User') -> bool:
        pass

    def addToWishlist(self, game: Game) -> bool:
        pass

    def removeFromWishlist(self, game: Game) -> bool:
        pass

    def writeReview(self, game: Game, content: str, rating: int) -> Review:
        pass

    def likeReview(self, review: Review):
        pass

    def dislikeReview(self, review: Review):
        pass

    def addSuggestion(self, game: Game, content: str) -> Suggestion:
        pass

    def managePreferences(self, preferences: Preferences):
        pass
