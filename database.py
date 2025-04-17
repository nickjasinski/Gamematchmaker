from user import User

class Database:
    def __init__(self, name: str, userID: int):
        self.name = name
        self.userID = userID

        # sample database to work from
        self.users = {
            "johndoe@example.com": User(1, "johndoe", "johndoe@test.com", "password123"),
            "janedoe@example.com": User(2, "janedoe", "janedoe@test.com", "password321")
        }

    def getUser(self, email: str) -> User:
        return self.users.get(email)

    def getProfile():
        pass

    def getGame():
        pass

    def getWishlist():
        pass
