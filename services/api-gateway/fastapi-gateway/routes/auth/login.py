from models.user import User  # Importa el modelo User
from config.database.sqlite import engine  # Importa la conexión de la base de datos
from sqlmodel import Session, select
from fastapi import HTTPException

# Lógica para manejar el inicio de sesión
def login_user(username: str, password: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")

        return {"message": "Inicio de sesión exitoso", "username": user.username}
