from user import User
from review import Review
from preferences import Preferences
from wishlist import Wishlist
from suggestion import Suggestion
from friend import Friend
from abstract_db import AbstractDB
from abstract_data_handler import AbstractDataHandler

class PostgresHandler(AbstractDataHandler):

    def __init__(self, postgres: AbstractDB):
        self.postgres = postgres

    def saveUser(self, user):
        cursor = self.postgres.getSession()
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            RETURNING user_id
        """, (user.username, user.email, user.password))
        user_id = cursor.fetchone()['user_id']
        self.postgres.getConnection().commit()
        user.userID = user_id
        return user

    def saveProfile(self, profile):
        cursor = self.postgres.getSession()
        cursor.execute("""
            UPDATE profiles
            SET name = %s, favorite_game = %s, bio = %s
            WHERE user_id = %s
        """, (profile.name, profile.favorite_game, profile.bio, profile.user.userID))
        self.postgres.getConnection().commit()

    def getProfile(self, user_id):
        cursor = self.postgres.getSession()
        cursor.execute("""
            SELECT * FROM profiles WHERE user_id = %s
        """, (user_id,))
        data = cursor.fetchone()
        return data

    def getUserByCredentials(self, email, password):
        cursor = self.postgres.getSession()
        cursor.execute("""
            SELECT * FROM users WHERE email = %s AND password = %s
        """, (email, password))
        result = cursor.fetchone()

        if result:
            from user import User
            user = User(
                userID=result['user_id'],
                username=result['username'],
                email=result['email'],
                password=result['password']
            )
            return user
        else:
            print("Invalid email or password.")
            return None

    def saveReview(self, review: Review):
        cursor = self.postgres.getSession()
        cursor.execute("""
        INSERT INTO reviews (user_id, game_id, content, rating)
        VALUES (%s, %s, %s, %s)
        RETURNING review_id
    """, (review.userID, review.gameID, review.content, review.rating))
    
        review_id = cursor.fetchone()['review_id']
        self.postgres.getConnection().commit()
        review.reviewId = review_id
    

    def savePreference(self, preferences: Preferences):
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

    def deletePreference(self, preferences: Preferences):
        pass

    def deleteWishlist(self, wishlist: Wishlist):
        pass

    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    def deleteFriend(self, friend: Friend):
        pass