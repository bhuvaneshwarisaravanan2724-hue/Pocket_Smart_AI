from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class ExpenseCreate(BaseModel):
    category: str
    amount: float
    description: str = ""


class ExpenseResponse(ExpenseCreate):
    id: int

    class Config:
        from_attributes = True