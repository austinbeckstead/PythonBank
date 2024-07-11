from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    balance: int = 0

    def editBalance(self, amount):
        self.balance += amount
