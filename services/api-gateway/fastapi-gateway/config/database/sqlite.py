import os
from sqlmodel import SQLModel, create_engine


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'database.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def init_db():
    SQLModel.metadata.create_all(engine)
