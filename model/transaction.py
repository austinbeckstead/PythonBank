from pydantic import BaseModel


class Transaction(BaseModel):
    authToken: str
    recipient: str
    amount: int