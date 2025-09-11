from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

    class Config:
        from_attributes = True