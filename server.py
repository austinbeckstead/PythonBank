from http.client import HTTPException
from typing import Union
from fastapi import FastAPI
from DataAccess.userDAO import UserDAO
from DataAccess.authDAO import AuthDAO
from model.transaction import Transaction
from model.user import User
from model.auth import Auth
from model.logout import Logout
from model.balanceUpdate import BalanceUpdate

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

@app.delete("/login/")
def logout(logout: Logout):
    auth_dao.removeAuth(logout.authToken)
    return {"message": "logged out"}

@app.put("/bank/")
def editBalance(update: BalanceUpdate):
    authToken = update.authToken
    amount = update.amount
    authData = auth_dao.getAuth(authToken)
    if authData != None:
        user = user_dao.getUser(authData.username)
        user.editBalance(amount)
        return {"message": "Current Balance: " + str(user.balance), "authToken": auth_dao.createAuth(user.username)}
    else:
        raise HTTPException(status_code=401, detail="Could not authenticate")

@app.post("/bank/")
def transaction(transaction: Transaction):
    authToken = transaction.authToken
    amount = transaction.amount
    recipientName = transaction.recipient
    authData = auth_dao.getAuth(authToken)
    if authData != None:
        user = user_dao.getUser(authData.username)
        recipient = user_dao.getUser(recipientName)
        if recipient != None:
            user.editBalance(amount * -1)
            recipient.editBalance(amount)
            return {"message": "Success! Current Balance: " + str(user.balance), "authToken": auth_dao.createAuth(user.username)}
        else:
            raise HTTPException(status_code=401, detail="Invalid recipient")

    else: 
        raise HTTPException(status_code=401, detail="Could not authenticate")







