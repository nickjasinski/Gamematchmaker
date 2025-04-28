import requests
from typing import List, Optional, Dict

from api_abstract import APIAbstract

class IGDBFetcher(APIAbstract):
    """Handles all raw API communication with IGDB"""
    def __init__(self):
        self.client_id = 'yr9ttfd7f5s3xyncki7zvzvetlajwa'
        self.access_token = 'bdi9rpdoyqp4lo1qel82f7b6ng2ple'
        self.base_url = 'https://api.igdb.com/v4/games'
        self.headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}'
        }

    def fetch_games_by_query(self, query: str) -> Optional[List[Dict]]:
        """Low-level API request that returns raw JSON data"""
        try:
            response = requests.post(self.base_url, headers=self.headers, data=query)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None