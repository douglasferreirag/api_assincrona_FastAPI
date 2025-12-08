from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.auth import Login, Token
from src.services.account import verify_credentials, create_account, get_account_by_email
from src.controllers import get_db
from src.security import create_access_token
from src.schemas.account import AccountCreate, AccountOut

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(data: Login, db: AsyncSession = Depends(get_db)):
    account = await verify_credentials(db, data.email, data.password)
    token = create_access_token({"sub": account.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", response_model=AccountOut)
async def register(data: AccountCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_account_by_email(db, data.email)
    if existing:
        from fastapi import HTTPException, status
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "E-mail já cadastrado")
    acc = await create_account(db, data.name, data.email, data.password)
    return acc
