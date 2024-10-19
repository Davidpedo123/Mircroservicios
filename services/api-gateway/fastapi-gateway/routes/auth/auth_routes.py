from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .auth_jwt import create_access_token, get_current_user, Token
from .login import login_user  # Asegúrate de que login_user esté correctamente importado
from models.user import Users
from sqlmodel import Session, select
from config.database.sqlite import engine

router_auth = APIRouter()

@router_auth.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Aquí se recibe el nombre de usuario y la contraseña desde el formulario
    user = login_user(form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
