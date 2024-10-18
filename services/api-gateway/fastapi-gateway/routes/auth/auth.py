from fastapi import APIRouter, Depends
from routes.auth.login import login_user  # Importa la lógica del login
from fastapi import Depends

router = APIRouter()

# Define la ruta para el login
@router.post("/login")
def login(username: str, password: str):
    return login_user(username, password)
