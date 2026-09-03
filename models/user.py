from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True



# Responses
class GetUsersResponse(BaseModel):
    users: List[User]

class CreateUserResponse(BaseModel):
    message:str
    user:User

class DeleteUserResponse(BaseModel):
    message:str

class UpdateUserResponse(BaseModel):
    message:str
    user:User