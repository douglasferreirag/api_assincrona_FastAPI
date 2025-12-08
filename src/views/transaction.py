from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def transaction_view():
    return {"message": "Views - Transactions. Use /api/transactions for API endpoints."}
