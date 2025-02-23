from model.user import User;

class UserDAO:
    def __init__(self):
        self.userData = {}
    
    def clear(self):
        self.userData = {}

    def getUser(self, username: str):
        return self.userData.get(username)

    def registerUser(self, user: User):
        self.userData[user.username] = user

    def verifyPassword(self, username: str, password: str):
        if self.userData.get(username) == None:
            return False
        return password == self.userData.get(username).password

