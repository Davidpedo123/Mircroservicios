# fastapi-gateway/models/user.py

from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # ID del usuario, clave primaria
    username: str = Field(index=True)  # Nombre de usuario, índice para búsquedas rápidas
    password: str  # Contraseña del usuario

    
