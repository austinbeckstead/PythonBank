from pydantic import BaseModel
from model.auth import Auth


class BalanceUpdate(BaseModel):
    authToken: str
    amount: int