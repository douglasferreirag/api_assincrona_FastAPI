from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.account import Account
from src.security import get_password_hash, verify_password
from src.exceptions import not_found, bad_request

async def create_account(db: AsyncSession, name: str, email: str, password: str) -> Account:
    hashed = get_password_hash(password)
    new = Account(name=name, email=email, hashed_password=hashed, balance=0.0)
    db.add(new)
    await db.commit()
    await db.refresh(new)
    return new

async def get_account_by_email(db: AsyncSession, email: str) -> Account | None:
    q = await db.execute(select(Account).where(Account.email == email))
    return q.scalars().first()

async def get_account_by_id(db: AsyncSession, account_id: int) -> Account | None:
    q = await db.execute(select(Account).where(Account.id == account_id))
    return q.scalars().first()

async def verify_credentials(db: AsyncSession, email: str, password: str) -> Account:
    account = await get_account_by_email(db, email)
    if not account:
        raise not_found("Conta não encontrada")
    if not verify_password(password, account.hashed_password):
        raise bad_request("Credenciais inválidas")
    return account
