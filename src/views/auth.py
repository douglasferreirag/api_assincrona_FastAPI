from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def auth_view():
    return {"message": "Views - Auth. Use /api/auth for endpoints (login/register)."}
