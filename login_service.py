
class LoginService:
    def __init__(self, email: str, password: str, userid: int):
        self.email = email
        self.password = password
        self.userid = userid

    def isRegistered(self, email: str, password: str):
        pass
