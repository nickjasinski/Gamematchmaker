from abc import ABC, abstractmethod
from game import Game

class APIAbstract(ABC):

    @abstractmethod
    def __init__(self, game: Game):
        self.game = game

    @abstractmethod
    def queryGame(id: int):
        pass