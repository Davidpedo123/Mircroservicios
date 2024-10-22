from fastapi import APIRouter, Depends, Header, HTTPException, Request
from ..auth.auth_jwt import get_current_user
 # Importa la función login_user
from .products import ProductsRequest, products
from sqlmodel import Session, select
from config.database.sqlite import engine
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


limiter = Limiter(key_func=get_remote_address)

router_product = APIRouter()



@router_product.get("/items", response_model=dict)
@limiter.limit("100/minute")
async def products_user(request: Request, authorization: str = Header(None), current_user: str = Depends(get_current_user)):
    return products()
    
