from pydantic import BaseModel, EmailStr, Field

class AccountCreate(BaseModel):
    name: str = Field(..., example="João Silva")
    email: EmailStr
    password: str = Field(..., min_length=6)

class AccountOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    balance: float

    class Config:
        orm_mode = True
