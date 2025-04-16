from user import User
from review import Review
from preference import Preference
from wishlist import Wishlist
from suggestion import Suggestion
from friend import Friend
from abstract_db import AbstractDB
from abstract_datahandler import AbstractDataHandler

class PostgresHandler(AbstractDataHandler):

    def __init__(self, db):
        super().__init__(db)

    def saveUser(self, user: User):
        pass

    def saveReview(self, review: Review):
        pass

    def savePreference(self, preference: Preference):
        pass

    def saveWishlist(self, wishlist: Wishlist):
        pass

    def saveSuggestion(self, suggestion: Suggestion):
        pass

    def saveFriend(self, friend: Friend):
        pass


    def deleteUser(self, user: User):
        pass

    def deleteReview(self, review: Review):
        pass

    def deletePreference(self, preference: Preference):
        pass

    def deleteWishlist(self, wishlist: Wishlist):
        pass

    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    def deleteFriend(self, friend: Friend):
        pass