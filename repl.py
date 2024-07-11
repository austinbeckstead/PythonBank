import client

status = "0"
authToken = None

while(status != "quit"):
    if authToken != None:
        userInput = input(" 1: Check Balance\n 2: Earn Money\n 3: Spend Money\n 4: Pay Someone\n 5: Logout\n" )
        if userInput == "1":
            authToken = client.editBalance(authToken, 0)
        if userInput == "2":
            amount = input("Amount: ")
            authToken = client.editBalance(authToken, int(amount))
        elif userInput == "3":
            amount = input("Amount: ")
            authToken = client.editBalance(authToken, int(amount)*-1)
        elif userInput == "4":
            recipient = input("Recipient: ")
            amount = input("Amount: ")
            client.transaction(authToken, recipient, int(amount))
        elif userInput == "5":
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
