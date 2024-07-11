from http.client import HTTPException
from typing import Union
from fastapi import FastAPI
from DataAccess.userDAO import UserDAO
from DataAccess.authDAO import AuthDAO
from user import User
from auth import Auth

app = FastAPI()
user_dao = UserDAO()
auth_dao = AuthDAO()

@app.post("/users/")
def create_user(user: User):
    if user_dao.getUser(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_dao.registerUser(user)
    return {"message": "User " + user.username +  " created successfully", "authToken": auth_dao.createAuth(user.username)}


@app.post("/login/")
def login(user:User):
    if user_dao.verifyPassword(user.username, user.password):
        return {"message": user.username + " logged in successfully", "authToken": auth_dao.createAuth(user.username)}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.delete("/login")
def logout(authToken: Auth):
    auth_dao.removeAuth(authToken.token)
    return {"message": authToken.username + " logged out"}



