from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    company : str
    designation : str
    password: str
    role : str
    type : str
    
class Admin(BaseModel):
    name: str
    email: str
    company : str
    designation : str
    password: str
    role : str = 'admin'
    type : str = None


class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]
    company: Optional[str]
    designation: Optional[str]
    password: Optional[str]

class UpdateAdmin(BaseModel):
    name: Optional[str]
    email: Optional[str]
    company: Optional[str]
    designation: Optional[str]
    password: Optional[str]