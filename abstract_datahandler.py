from abc import ABC, abstractmethod
from user import User
from review import Review
from preference import Preference
from wishlist import Wishlist
from suggestion import Suggestion
from friend import Friend
from abstract_db import AbstractDB

class AbstractDataHandler(ABC):

    @abstractmethod
    def __init__(self, db: AbstractDB):
        self.db = db

    @abstractmethod
    def saveUser(self, user: User):
        pass

    @abstractmethod
    def saveReview(self, review: Review):
        pass

    @abstractmethod
    def savePreference(self, preference: Preference):
        pass

    @abstractmethod
    def saveWishlist(self, wishlist: Wishlist):
        pass

    @abstractmethod
    def saveSuggestion(self, suggestion: Suggestion):
        pass

    @abstractmethod
    def saveFriend(self, friend: Friend):
        pass

    @abstractmethod
    def deleteUser(self, user: User):
        pass

    @abstractmethod
    def deleteReview(self, review: Review):
        pass

    @abstractmethod
    def deletePreference(self, preference: Preference):
        pass

    @abstractmethod
    def deleteWishlist(self, wishlist: Wishlist):
        pass

    @abstractmethod
    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    @abstractmethod
    def deleteFriend(self, friend: Friend):
        pass
