from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    __tablename__ = "users"  # Esto define explícitamente el nombre de la tabla

    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str
