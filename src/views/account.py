from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def account_view():
    return {"message": "Views - Accounts. Use /api/accounts for API endpoints."}
