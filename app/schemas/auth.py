from pydantic import BaseModel
from pip._vendor.rich.prompt import password

class LoginRequest(BaseModel):
    identifier: str
    password: str
    
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"