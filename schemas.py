from pydantic import BaseModel


class Message(BaseModel):
    user_id: int = 111111111
    text: str
