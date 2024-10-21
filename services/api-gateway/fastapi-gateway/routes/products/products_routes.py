from fastapi import APIRouter, Depends, Header, HTTPException
from ..auth.auth_jwt import get_current_user
 # Importa la función login_user
from .products import ProductsRequest, products
from sqlmodel import Session, select
from config.database.sqlite import engine

router_product = APIRouter()



@router_product.get("/items", response_model=dict)
def products_user(authorization: str = Header(None), current_user: str = Depends(get_current_user)):
    return products()
    
