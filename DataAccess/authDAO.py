import uuid
from auth import Auth;

class AuthDAO:
    def __init__(self):
        self.authData = {}
    
    def clear(self):
        self.authData = {}

    def createAuth(self, username: str):
        authToken = Auth(username=username, token=str(uuid.uuid4()))
        self.authData[authToken.token] = authToken
        return authToken

    def getAuth(self, token: str):
        return self.authData.get(token)

    def removeAuth(self, token: str):
        self.authData.pop(token)

