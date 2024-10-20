from fastapi import APIRouter, Depends, Body, Header, HTTPException
from ..auth.auth_jwt import get_current_user  # Asegúrate de tener esto bien configurado
from .user_example import UserMontoRequest, user_example  # Asegúrate de importar tu modelo
from models.user import Users  # Importa el modelo Users
from sqlmodel import Session
from config.database.sqlite import engine


router_users = APIRouter()

@router_users.get("/monto", response_model=dict)
def set_monto(authorization: str = Header(None),current_user: Users = Depends(get_current_user)):
    return user_example()
