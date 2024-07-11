import requests
from requests.exceptions import HTTPError
from user import User
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

def logout_user(token: str):
        url = f"{BASE_URL}/login/"
        responseString  = requests.delete(url, json=token)
        return readResponse(responseString)

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
    