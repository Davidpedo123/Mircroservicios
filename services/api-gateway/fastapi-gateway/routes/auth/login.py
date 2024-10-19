from models.user import Users  # Importa el modelo User
from config.database.sqlite import engine  # Importa la conexión de la base de datos
from sqlmodel import Session, select
from fastapi import HTTPException
from pydantic import BaseModel

# Clase que define los datos de la solicitud de login
class LoginRequest(BaseModel):
    username: str
    password: str

# Lógica para manejar el inicio de sesión
def login_user(username: str, password: str):
    with Session(engine) as session:
        statement = select(Users).where(Users.username == username)
        user = session.exec(statement).first()

        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")

        return user
