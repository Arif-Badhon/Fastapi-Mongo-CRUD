from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: Optional[str]
    email: Optional[str]
    company : Optional[str]
    designation : Optional[str]
    password: Optional[str]
    role : Optional[str]
    type : Optional[str]
    
class Admin(BaseModel):
    name: Optional[str]
    email: Optional[str]
    company : Optional[str]
    designation : Optional[str]
    password: Optional[str]
    role : Optional[str] = 'admin'
    type : Optional[str] = None
