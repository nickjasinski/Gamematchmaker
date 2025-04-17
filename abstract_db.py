from abc import ABC, abstractmethod

class AbstractDB(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def getSession(self):
        pass

    @abstractmethod
    def getConnection(self):
        pass
    