import os
from sqlmodel import SQLModel, create_engine

# Define la ruta del directorio raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define la URL de la base de datos SQLite
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'database.db')}"

# Crea el motor de conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crea una función para inicializar la base de datos
def init_db():
    SQLModel.metadata.create_all(engine)
