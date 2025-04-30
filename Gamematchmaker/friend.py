from user import User

class Friend:
    def __init__(self, user: User, friend: User):
        self.user = user
        self.friend = friend

    def add(self):
        self.user.addFriend(self.friend)
        self.friend.addFriend(self.user)
        print(f"{self.user.username} and {self.friend.username} are now friends.")

    def remove(self):
        self.user.removeFriend(self.friend)
        self.friend.removeFriend(self.user)
        print(f"{self.user.username} and {self.friend.username} are no longer friends.")
