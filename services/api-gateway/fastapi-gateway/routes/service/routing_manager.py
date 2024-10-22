from fastapi import APIRouter, Depends, Request
from .service_example import hellowork 
import httpx
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import Depends


limiter = Limiter(key_func=get_remote_address)

manager_routing = APIRouter()

# Define la ruta para el login
@manager_routing.get("/service1")
@limiter.limit("100/minute")
async def service1(request: Request):
    return await hellowork()  # Usa await aquí

