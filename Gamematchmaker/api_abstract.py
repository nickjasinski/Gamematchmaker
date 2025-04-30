from abc import ABC, abstractmethod
from typing import List, Optional
from game import Game

class APIAbstract(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fetch_games_by_query(self, query: str) -> Optional[List[dict]]:
        pass