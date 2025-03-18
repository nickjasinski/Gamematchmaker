from user import User

class Friend:
    def __init__(self, friendId: int):
        self.friendId = friendId

    def sendRequest(self, friend: User) -> bool:
        pass

    def acceptRequest(self, friend: User) -> bool:
        pass

    def rejectRequest(self, friend: User) -> bool:
        pass