from game import Game
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

    # Saves the user to the database
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

    # Saves the profile to the database
    def saveProfile(self, profile):
        cursor = self.postgres.getSession()
        cursor.execute("""
            UPDATE profiles
            SET name = %s, favorite_game = %s, bio = %s
            WHERE user_id = %s
        """, (profile.name, profile.favorite_game, profile.bio, profile.user.userID))
        self.postgres.getConnection().commit()

    # Fetches the profile for the specified user_id from the database
    def getProfile(self, user_id):
        cursor = self.postgres.getSession()
        cursor.execute("""
            SELECT * FROM profiles WHERE user_id = %s
        """, (user_id,))
        data = cursor.fetchone()
        return data

    # Fetches the user from the database by email and password
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

    # Save review to the database
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

    #Adds a like to the review in the database
    def likeReview(self, review: Review):
        cursor = self.postgres.getSession()
        cursor.execute("""
        UPDATE reviews
        SET likes = likes + 1
        WHERE review_id = %s
        """, (review.reviewId,))
        
        self.postgres.getConnection().commit()

    #Adds a dislike to the review in the database
    def dislikeReview(self, review: Review):
        cursor = self.postgres.getSession()
        cursor.execute("""
        UPDATE reviews
        SET dislikes = dislikes + 1
        WHERE review_id = %s
        """, (review.reviewId,))

        self.postgres.getConnection().commit()
    
    #Fetches the review by ID from the database
    def getReviewById(self, review_id: int):
        cursor = self.postgres.getSession()
        cursor.execute("""
        SELECT * FROM reviews WHERE review_id = %s
        """, (review_id,))
        result = cursor.fetchone()
    
        if result:
            return Review(
                reviewId=result['review_id'],
                userID=result['user_id'],
                gameID=result['game_id'],
                content=result['content'],
                rating=result['rating'],
                likes=result.get('likes', 0),
                dislikes=result.get('dislikes', 0)
            )
        else:
            return None

    def savePreference(self, preferences: Preferences):
        pass

    # Fetches the wishlist for the specified user_id from the database
    def getWishlist(self, user_id: int) -> list:
        """Fetches the wishlist for the specified user from the database"""
        cursor = self.postgres.getSession()
        cursor.execute("""
            SELECT wishlist
            FROM users
            WHERE user_id = %s
        """, (user_id,))
        result = cursor.fetchone()
        return result['wishlist'] if result and result['wishlist'] else []

    # Saves the wishlist to the database for the specified user_id
    def saveWishlist(self, wishlist: Wishlist, user_id: int):
        """Saves the wishlist to the database for the specified user"""
        cursor = self.postgres.getSession()
        cursor.execute("""
            UPDATE users
            SET wishlist = %s
            WHERE user_id = %s
        """, (wishlist.games, user_id))
        self.postgres.getConnection().commit()

    def saveSuggestion(self, suggestion: Suggestion):
        pass

    def saveFriend(self, friend: Friend):
        cursor = self.postgres.getSession()
        cursor.execute("""
            INSERT INTO friends (user_id, friend_id)
            VALUES (%s, %s), (%s, %s)
            ON CONFLICT DO NOTHING
        """, (
            friend.user.userID, friend.friend.userID,
            friend.friend.userID, friend.user.userID 
        ))
        self.postgres.getConnection().commit()

    def getUserByEmail(self, email):
        cursor = self.postgres.getSession()
        cursor.execute("""
            SELECT * FROM users WHERE email = %s
        """, (email,))
        result = cursor.fetchone()

        if result:
            from user import User
            return User(
                userID=result['user_id'],
                username=result['username'],
                email=result['email'],
                password=result['password']
            )
        else:
            return None

    def deleteUser(self, user: User):
        pass

    def deleteReview(self, review: Review):
        pass

    def deletePreference(self, preferences: Preferences):
        pass

    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    def deleteFriend(self, friend: Friend):
        cursor = self.postgres.getSession()
        cursor.execute("""
            DELETE FROM friends
            WHERE (user_id = %s AND friend_id = %s)
            OR (user_id = %s AND friend_id = %s)
        """, (
            friend.user.userID, friend.friend.userID,
            friend.friend.userID, friend.user.userID
        ))
        self.postgres.getConnection().commit()