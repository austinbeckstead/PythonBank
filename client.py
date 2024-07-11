import requests
from requests.exceptions import HTTPError
from model.transaction import Transaction
from model.user import User
from model.balanceUpdate import BalanceUpdate
from model.auth import Auth
from model.logout import Logout

BASE_URL = "http://localhost:8000"


def create_user(username, password):
    url = f"{BASE_URL}/users/"
    newUser = User(username=username, password=password)
    try:
        responseString = requests.post(url, json=newUser.dict())
        return readResponse(responseString)
    except Exception as err:
        print("Username " + username + " Taken")
        return None

def login_user(username, password):
        url = f"{BASE_URL}/login/"
        credentials = User(username=username, password=password)
        try:
            responseString  = requests.post(url, json=credentials.dict())
            return readResponse(responseString)
        except Exception as err:
            print("Invalid Credentials")
            return None

def logout_user(token: Auth):
        url = f"{BASE_URL}/login/"
        logout = Logout(authToken=Auth(**token).token)
        responseString  = requests.delete(url, json=logout.dict())
        return readResponse(responseString)

def editBalance(token: Auth, amount: int):
    url = f"{BASE_URL}/bank/"
    update = BalanceUpdate(authToken = Auth(**token).token, amount=amount)
    try:
        responseString = requests.put(url, json=update.dict())
        return readResponse(responseString)
    except Exception as err:
        print("Could Not Authenticate")
        return None

def transaction(token: Auth, recipient: str, amount: int):
    url = f"{BASE_URL}/bank/"
    transaction = Transaction(authToken = Auth(**token).token, recipient=recipient, amount=amount)    
    try:
        responseString = requests.post(url, json=transaction.dict())
        return readResponse(responseString)
    except Exception as err:
        print("Could Not Authenticate")
        return None

def readResponse(responseString):
    response = responseString.json()
    if "message" in response:
        print(response["message"])
    if "authToken" in response:
        authToken = response["authToken"]
        return authToken



"""
response = create_user("Dude2", "password")
if "message" in response:
    print(response["message"])
if "authToken" in response:
    authToken = response["authToken"]
else:
    print(response)

"""
    