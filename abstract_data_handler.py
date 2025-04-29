from abc import ABC, abstractmethod
from user import User
from review import Review
from preferences import Preferences
from wishlist import Wishlist
from suggestion import Suggestion
from friend import Friend
from abstract_db import AbstractDB

class AbstractDataHandler(ABC):

    @abstractmethod
    def __init__(self, postgres: AbstractDB):
        pass

    @abstractmethod
    def saveUser(self, user: User):
        pass

    @abstractmethod
    def saveReview(self, review: Review):
        pass

    @abstractmethod
    def savePreference(self, preferences: Preferences):
        pass

    @abstractmethod
    def saveWishlist(self, wishlist: Wishlist, user_id: int):
        pass

    @abstractmethod
    def saveSuggestion(self, suggestion: Suggestion):
        pass

    @abstractmethod
    def saveFriend(self, friend: Friend):
        pass

    @abstractmethod
    def saveProfile(self, profile):
        pass

    @abstractmethod
    def likeReview(self, review: Review):
        pass

    @abstractmethod
    def dislikeReview(self, review: Review):
        pass

    @abstractmethod
    def deleteUser(self, user: User):
        pass

    @abstractmethod
    def deleteReview(self, review: Review):
        pass

    @abstractmethod
    def deletePreference(self, preferences: Preferences):
        pass

    @abstractmethod
    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    @abstractmethod
    def deleteFriend(self, friend: Friend):
        pass

    @abstractmethod
    def getProfile(self, user_id): 
        pass

    @abstractmethod
    def getUserByCredentials(self, email, password): 
        pass

    @abstractmethod
    def getReviewById(self, review_id: int):
        pass