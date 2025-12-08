from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers import get_db
from src.schemas.transaction import TransactionCreate, TransactionOut
from src.services.transaction import create_transaction, get_transactions_by_account

router = APIRouter()

@router.post("/account/{account_id}", response_model=TransactionOut)
async def post_transaction(account_id: int, payload: TransactionCreate, db: AsyncSession = Depends(get_db)):
    trans = await create_transaction(db, account_id, payload.type, payload.amount)
    return trans

@router.get("/account/{account_id}", response_model=list[TransactionOut])
async def get_account_transactions(account_id: int, db: AsyncSession = Depends(get_db)):
    return await get_transactions_by_account(db, account_id)
