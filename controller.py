from igdb_fetcher import IGDBFetcher
from game_service import GameService
from user import User

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
