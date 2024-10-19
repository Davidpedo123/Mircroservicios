

from pydantic import BaseModel

class UserMontoRequest(BaseModel):
    dinero: int

def user_example():
	return {"dinero": 1000}