import client

status = "0"
authToken = None

while(status != "quit"):
    if authToken != None:
        userInput = input(" 1: Logout\n" )
        if userInput == "1":
            authToken = client.logout_user(authToken)
    else:
        userInput = input(" 1: Login \n 2: Register \n 3: Quit\n" )
        if userInput == "1":
            username = input("Username: ")
            password = input("Password: ")
            authToken = client.login_user(username, password)
        elif userInput == "2":
            username = input("Username: ")
            password = input("Password: ")
            authToken = client.create_user(username, password)
        elif userInput == "3":
            status = "quit"
        else:
            ...
