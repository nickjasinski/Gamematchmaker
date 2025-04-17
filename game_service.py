from datetime import datetime
from typing import List, Dict, Optional
from igdb_fetcher import IGDBFetcher
from game import Game  

class GameService:
    """Handles business logic and Game object creation"""
    def __init__(self, fetcher: IGDBFetcher):
        self.fetcher = fetcher

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

    def _create_game_object(self, game_data: Dict) -> Game:
        """Helper: Converts raw API data into Game objects"""
        return Game(
            name=game_data.get('name', 'Unknown'),
            genres=[g['name'] for g in game_data.get('genres', []) if 'name' in g],
            platforms=[p['name'] for p in game_data.get('platforms', []) if 'name' in p],
            release_date=self._parse_date(game_data.get('release_dates', [])),
            rating=game_data.get('rating'),  # IGDB ratings are optional
            summary=game_data.get('summary')
        )

    def _parse_date(self, release_dates: List[Dict]) -> Optional[datetime.date]:
        """Helper: Converts IGDB timestamp to date object"""
        if release_dates and release_dates[0].get('date'):
            return datetime.fromtimestamp(release_dates[0]['date']).date()
        return None
