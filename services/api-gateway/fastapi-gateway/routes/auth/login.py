from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from models.user import User  # Importa el modelo de usuario
from config.database.sqlite import get_session  # Importa la función de sesión de la base de datos
from pydantic import BaseModel

# Crear el enrutador de FastAPI
router = APIRouter()

# Esquema para los datos que se enviarán en el cuerpo de la solicitud
class LoginRequest(BaseModel):
    username: str
    password: str

# Ruta para manejar el login
@router.post("/login", response_model=str)  # Respuesta simplificada solo con un mensaje
def login(request: LoginRequest, session: Session = Depends(get_session)):
    # Buscar al usuario por nombre de usuario
    statement = select(User).where(User.username == request.username)
    user = session.exec(statement).first()

    # Validar si el usuario existe
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    # Validar la contraseña
    if user.password != request.password:  # Nota: esto es solo un ejemplo simple, deberías usar un hash seguro
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Contraseña incorrecta")

    return f"Bienvenido, {user.username}!"  # Respuesta en caso de login exitoso
