from sqlalchemy.ext.asyncio import AsyncSession
from src.models.transaction import Transaction
from src.models.account import Account
from src.exceptions import bad_request, not_found
from sqlalchemy import select

async def create_transaction(db: AsyncSession, account_id: int, t_type: str, amount: float) -> Transaction:
    # pega account
    q = await db.execute(select(Account).where(Account.id == account_id))
    account = q.scalars().first()
    if not account:
        raise not_found("Conta não encontrada")

    if amount <= 0:
        raise bad_request("O valor da transação deve ser positivo")

    if t_type == "withdraw":
        if account.balance < amount:
            raise bad_request("Saldo insuficiente")
        account.balance -= amount
    elif t_type == "deposit":
        account.balance += amount
    else:
        raise bad_request("Tipo de transação inválido")

    trans = Transaction(account_id=account_id, type=t_type, amount=amount)
    db.add(trans)
    db.add(account)
    await db.commit()
    await db.refresh(trans)
    return trans

async def get_transactions_by_account(db: AsyncSession, account_id: int):
    q = await db.execute(select(Transaction).where(Transaction.account_id == account_id).order_by(Transaction.created_at.desc()))
    return q.scalars().all()
