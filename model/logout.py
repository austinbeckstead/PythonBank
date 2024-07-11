from pydantic import BaseModel
from model.auth import Auth


class Logout(BaseModel):
    authToken: str
