from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    __tablename__ = "users"  

    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str
