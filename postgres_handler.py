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
        # Validate user data
        if not user.username or not user.email or not user.password:
            raise ValueError("Invalid user data: username, email, and password are required.")

        session = self.postgres.getSession()
        try:
            session.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
                RETURNING user_id
                """,
                (user.username, user.email, user.password)
            )
            user_id = session.fetchone()["user_id"]
            self.postgres.getConnection().commit()
            user.userID = user_id
            return user
        except Exception as e:
            self.postgres.getConnection().rollback()
            raise e

    # Saves the profile to the database
    def saveProfile(self, profile):
        cursor = self.postgres.getSession()
        cursor.execute("""
            INSERT INTO profiles (user_id, name, favorite_game, bio)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id)
            DO UPDATE SET name = EXCLUDED.name,
                          favorite_game = EXCLUDED.favorite_game,
                          bio = EXCLUDED.bio
        """, (profile.user.userID, profile.name, profile.favorite_game, profile.bio))
        self.postgres.getConnection().commit()

    # Deletes the profile from the database
    def deleteProfile(self, user_id: int):
        cursor = self.postgres.getSession()
        cursor.execute("""
            DELETE FROM profiles
            WHERE user_id = %s
        """, (user_id,))
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

    def saveFriend(self, user: User, friend: User):
        cursor = self.postgres.getSession()

        # Get current friend list
        cursor.execute("""
            SELECT friends FROM users WHERE user_id = %s
        """, (user.userID,))
        result = cursor.fetchone()
        current_friends = result['friends'] if result and result['friends'] else []

        # Avoid duplicates
        if friend.email not in current_friends:
            current_friends.append(friend.email)
            cursor.execute("""
                UPDATE users SET friends = %s WHERE user_id = %s
            """, (current_friends, user.userID))
            self.postgres.getConnection().commit()

    def deleteUser(self, user: User):
        pass

    def deleteReview(self, review: Review):
        pass

    def deletePreference(self, preferences: Preferences):
        pass

    def deleteSuggestion(self, suggestion: Suggestion):
        pass

    def deleteFriend(self, user: User, friend: User):
        cursor = self.postgres.getSession()

        # Get current friends
        cursor.execute("""
            SELECT friends FROM users WHERE user_id = %s
        """, (user.userID,))
        result = cursor.fetchone()
        current_friends = result['friends'] if result and result['friends'] else []

        # Remove if exists
        if friend.email in current_friends:
            current_friends.remove(friend.email)
            cursor.execute("""
                UPDATE users SET friends = %s WHERE user_id = %s
            """, (current_friends, user.userID))
            self.postgres.getConnection().commit()

    def getFriends(self, user: User) -> list:
        cursor = self.postgres.getSession()
        
        # Get list of friend emails
        cursor.execute("""
            SELECT friends FROM users WHERE user_id = %s
        """, (user.userID,))
        result = cursor.fetchone()
        emails = result['friends'] if result and result['friends'] else []

        # Now fetch user info for each friend email
        if not emails:
            return []

        query = """
            SELECT username, email FROM users
            WHERE email = ANY(%s)
        """
        cursor.execute(query, (emails,))
        rows = cursor.fetchall()

        from user import User
        return [User(None, row['username'], row['email'], None) for row in rows]


    #helper function
    def getUserByEmail(self, email):
        cursor = self.postgres.getSession()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result:
            return User(
                userID=result['user_id'],
                username=result['username'],
                email=result['email'],
                password=result['password']
            )
        return None