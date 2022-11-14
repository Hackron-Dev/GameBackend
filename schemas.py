from pydantic import BaseModel


class User_(BaseModel):
    Login_: str
    Password_: str
    score_: str = 0
