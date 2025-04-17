from database import Database 

class LoginService:
    # def __init__(self, email: str, password: str, userid: int):
    #     self.email = email
    #     self.password = password
    #     self.userid = userid
    def __init__(self):
        self.db = Database("GameMatchmakerDB", 0)  # Creating database object


    def isRegistered(self, email: str, password: str):
        user = self.db.getUser(email)

        if user is None:
            print("\n User not found.")
            return False
        
        if user.password == password:
            print("\n Login successful!")
            return True
        else:
            print("\n Incorrect password.")
            return False
