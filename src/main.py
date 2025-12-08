from fastapi import FastAPI
from src.config import settings
from src.database import engine, init_models
from src.controllers import account as account_controller
from src.controllers import auth as auth_controller
from src.controllers import transaction as transaction_controller
from src.views import account as account_view, auth as auth_view, transaction as transaction_view

app = FastAPI(title="API Bancária Assíncrona")

# inclui routers
app.include_router(auth_controller.router, prefix="/api/auth", tags=["auth"])
app.include_router(account_controller.router, prefix="/api/accounts", tags=["accounts"])
app.include_router(transaction_controller.router, prefix="/api/transactions", tags=["transactions"])

# views (simples páginas de teste)
app.include_router(auth_view.router, prefix="/views/auth", tags=["views"])
app.include_router(account_view.router, prefix="/views/accounts", tags=["views"])
app.include_router(transaction_view.router, prefix="/views/transactions", tags=["views"])

@app.on_event("startup")
async def on_startup():
    # cria tabelas (apenas para desenvolvimento; em produção use migrations)
    await init_models()

@app.get("/")
async def health():
    return {"status": "ok", "app": "API Bancária Assíncrona"}
