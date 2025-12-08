from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers import get_db
from src.schemas.account import AccountOut
from src.services.account import get_account_by_id

router = APIRouter()

@router.get("/{account_id}", response_model=AccountOut)
async def get_account(account_id: int, db: AsyncSession = Depends(get_db)):
    acc = await get_account_by_id(db, account_id)
    if not acc:
        from fastapi import HTTPException, status
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Conta não encontrada")
    return acc
