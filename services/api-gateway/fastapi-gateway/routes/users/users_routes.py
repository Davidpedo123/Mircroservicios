from fastapi import APIRouter, Depends, Body, Header, HTTPException, Request
from ..auth.auth_jwt import get_current_user  # Asegúrate de tener esto bien configurado
from .user_example import UserMontoRequest, user_example  # Asegúrate de importar tu modelo
from models.user import Users  # Importa el modelo Users
from sqlmodel import Session
from config.database.sqlite import engine
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

router_users = APIRouter()

@router_users.get("/monto", response_model=dict)
@limiter.limit("100/minute")
def set_monto(request: Request, authorization: str = Header(None),current_user: Users = Depends(get_current_user)):
    return user_example()
