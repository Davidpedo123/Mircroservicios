from pydantic import BaseModel

# Clase que define los datos de la solicitud de login
class ProductsRequest(BaseModel):
    product: str
    id: int

def products():
    return {"Products": "banano", "id": 1}