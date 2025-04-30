from igdb_fetcher import IGDBFetcher
from game_service import GameService
from user import User
import wishlist
from wishlist_service import WishlistService

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


    def displayProfile(self, user):
        if user.profile:
            profile = user.profile
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

    def search_game_by_title_return_game(self, title):
        fetcher = IGDBFetcher()
        service = GameService(fetcher)

        games = service.search_games(title)
    
        if games:
            return games[0] 
        else:
            return None