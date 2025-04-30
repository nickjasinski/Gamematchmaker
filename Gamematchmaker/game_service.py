from datetime import datetime
from difflib import SequenceMatcher
from typing import List, Dict, Optional
from igdb_fetcher import IGDBFetcher
from game import Game  

class GameService:
    """Handles business logic and Game object creation"""
    def __init__(self, fetcher: IGDBFetcher):
        self.fetcher = fetcher

    # Search for games by title
    def search_games(self, title: str, limit: int = 5) -> List[Game]:
        """Returns fully constructed Game objects"""
        query = f"""
            fields name, genres.name, platforms.name, 
                   release_dates.date, rating, summary;
            search "{title}";
            limit {limit};
        """
        raw_games = self.fetcher.fetch_games_by_query(query)
        return [self._create_game_object(g) for g in raw_games]

    # Recommendation alogrithm
    def get_recommended_games(self, game_name: str) -> List[Game]:
        """
        Print all games in the same series (franchise) by name
        Return up to 5 games with at least 2 matching genres as full Game objects
        """
        # Fetch the target game details
        target_query = f"""
            fields name, genres.name, franchises.games, id;
            search \"{game_name}\";
            limit 1;
        """
        target_data = self.fetcher.fetch_games_by_query(target_query)

        if not target_data:
            return []

        target = target_data[0]
        target_id = target.get("id")
        target_genres = {g["name"] for g in target.get("genres", []) if isinstance(g, dict) and "name" in g}
        franchise_games_ids = target.get("franchises", [{}])[0].get("games", []) if "franchises" in target and isinstance(target.get("franchises"), list) else []

        # Fetch and print unique games from the same franchise
        print("OTHER GAMES IN THE FRANCHISE:\n")
        game_ids = sorted(set(str(gid) for gid in franchise_games_ids if gid != target_id))
        seen_names = set()
        if game_ids:
            game_details = self.get_game_names_by_ids(game_ids)
            for game in game_details:
                name = game.get("name")
                if name and name not in seen_names:
                    print(f"-{name}")
                    seen_names.add(name)

        # Fetch genre-based recommendations (at least 2 matching genres)
        genre_games: Dict[int, Dict] = {}
        if target_genres:
            genre_match_query = f"""
                fields name, genres.name, platforms.name, release_dates.date, rating, summary;
                where genres != null & id != {target_id};
                limit 100;
            """
            genre_candidates = self.fetcher.fetch_games_by_query(genre_match_query) or []
            for game in genre_candidates:
                game_genres = {g["name"] for g in game.get("genres", []) if isinstance(g, dict) and "name" in g}
                if len(game_genres & target_genres) >= 2:
                    genre_games[game["id"]] = game

       
        # Return top 5 genre-based Game objects
        print("\nGENRE-BASED RECOMMENDATIONS:\n")
        return [self._create_game_object(g) for g in list(genre_games.values())[:5]]

    # Helper function to fetch game names by IDs 
    def get_game_names_by_ids(self, game_ids: List[str]) -> List[Dict]:
        """Fetches full game data for a list of game IDs"""
        if not game_ids:
            return []

        game_details_query = f"""
            fields name, genres.name, platforms.name, release_dates.date, rating, summary;
            where id = ({','.join(game_ids)});
            limit {len(game_ids)};
        """
        return self.fetcher.fetch_games_by_query(game_details_query) or []

    # Helper function to create Game objects
    def _create_game_object(self, game_data: Dict) -> Game:
        """Properly creates Game object with data handling"""
        if not isinstance(game_data, dict):
            raise ValueError("Invalid game data format")
        genres = [g["name"] if isinstance(g, dict) else g for g in game_data.get("genres", [])]
        platforms = [p["name"] if isinstance(p, dict) else p for p in game_data.get("platforms", [])]
        release_date = None
        if "release_dates" in game_data:
            valid_dates = [d["date"] for d in game_data["release_dates"] if isinstance(d, dict) and "date" in d]
            if valid_dates:
                release_date = datetime.fromtimestamp(min(valid_dates)).date()

        return Game(
            gameID=game_data.get("id"),
            name=game_data.get("name", "Unknown"),
            genres=genres,
            platforms=platforms,
            release_date=release_date,
            rating=game_data.get("rating"),
            summary=game_data.get("summary")
        )

