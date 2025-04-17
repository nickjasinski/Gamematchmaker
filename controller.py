from igdb_fetcher import IGDBFetcher
from game_service import GameService

class Controller:
    def __init__(self):
        pass

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
            
        