from igdb_fetcher import IGDBFetcher
from game_service import GameService
from user import User
import wishlist
from wishlist_service import WishlistService
from review import Review

class Controller:
    def __init__(self):
        from database_factory import DatabaseFactory
        from profile_service import ProfileService

        self.data_handler = DatabaseFactory.getHandler()
        self.profile_service = ProfileService(self.data_handler)

    def signUp(self, username, email, password):
        user = User(None, username, email, password)
        return self.data_handler.saveUser(user)

    def logIn(self, email, password):
        return self.data_handler.getUserByCredentials(email, password)

    def editProfile(self, user, name, favorite_game, bio):
        return self.profile_service.editProfile(name, favorite_game, bio, user)

    def deleteProfile(self, user: User):
        self.data_handler.deleteProfile(user.userID)
        user.profile = None
        print("Profile deleted successfully.")

    def deleteProfile(self, user: User):
        success = self.profile_service.deleteProfile(user)
        if success:
            print("Profile deleted successfully.")
        else:
            print("Failed to delete profile.")


    def displayProfile(self, user):
        profile = self.profile_service.getProfile(user)

        if user.profile:
            print("\n--- Profile Information ---")
            print(f"Name: {profile.name}")
            print(f"Favorite Game: {profile.favorite_game}")
            print(f"Bio: {profile.bio}")
            print("-----------------------------\n")
        else:
            print("\nNo profile found for this user.\n")

    def search_game_by_title(self):
        """Search for a game by title"""
        fetcher = IGDBFetcher()
        service = GameService(fetcher)

        while True:
            search_term = input("\nEnter game title (or 'q' to quit): ").strip()
            if search_term.lower() == 'q':
                break
            print("\n")
            games = service.search_games(search_term)
            
            for game in games:
                print(game)
                print("-" * 150)

    def search_recommended_games(self):
        """Search for game recommendations"""
        fetcher = IGDBFetcher()
        service = GameService(fetcher)

        while True:
            search_term = input("\nEnter game title to find similar games (or 'q' to quit): ").strip()
            if search_term.lower() == 'q':
                break
            print("\n")
            recommendations = service.get_recommended_games(search_term)
            
            for game in recommendations:
                    print(game)
                    print("-" * 150)

    def manage_wishlist(self, user: User):
        """Manage user's wishlist"""
        service = WishlistService(self.data_handler)

        while True:
            print("\n--- Wishlist Management ---")
            print("1. Add game to wishlist")
            print("2. Remove game from wishlist")
            print("3. View wishlist")
            print("4. Back to main menu")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                game_title = input("\nEnter the title of the game to add: ")
                service.addGame(game_title, user.userID)
            elif choice == '2':
                game_title = input("\nEnter the title of the game to remove: ")
                service.removeGame(game_title, user.userID) 
            elif choice == '3':
                wishlist = service.getWishlist(user.userID)
                print("\n--- Your Wishlist ---")
                for game in wishlist.games:
                    print(f"- {game}")
            elif choice == '4':
                return

    def saveReview(self, review):
        self.data_handler.saveReview(review)

    def getReviewById(self, review_id):
        return self.data_handler.getReviewById(review_id)
    
    def likeReview(self, review):
        self.data_handler.likeReview(review)

    def dislikeReview(self, review):
        self.data_handler.dislikeReview(review)

    from review import Review

    def view_review_by_id(self, review_id):
        review = self.data_handler.getReviewById(int(review_id))  # make sure it's an int

        if review:
            print("\n--- Review Details ---")
            print(f"Review ID: {review.reviewId}")
            print(f"User ID: {review.userID}")
            print(f"Game Name: {review.gameName}")
            print(f"Content: {review.content}")
            print(f"Rating: {review.rating}/5")
            print(f"Likes: {review.likes}")
            print(f"Dislikes: {review.dislikes}")
            print("------------------------\n")
        else:
            print("No review found with that ID.\n")

    def writeReview(self, user: User, gameName: str, content: str, rating: int):
        review = Review(
            reviewId=None,
            userID=user.userID,
            gameName=gameName,
            content=content,
            rating=rating
        )
        self.saveReview(review)
        print("Review was submitted successfully!\n")

    def search_game_by_title_return_game(self, title):
        fetcher = IGDBFetcher()
        service = GameService(fetcher)

        games = service.search_games(title)
    
        if games:
            return games[0] 
        else:
            return None
        
    def addFriend(self, current_user: User, friend_user: User):
        self.data_handler.saveFriend(current_user, friend_user)
        print(f"\n{friend_user.username} has been added to your friend list.")

    def removeFriend(self, current_user: User, friend_user: User):
        self.data_handler.deleteFriend(current_user, friend_user)
        print(f"\n{friend_user.username} has been removed from your friend list.")

    def viewFriendsList(self, user: User):
        friends = self.data_handler.getFriends(user)
        if not friends:
            print("You have no friends added yet.\n")
            return

        print("\n--- Your Friends ---")
        for friend in friends:
            print(f"- {friend.username} ({friend.email})")
        print("---------------------\n")


    def get_user_by_email(self, email):
        return self.data_handler.getUserByEmail(email)