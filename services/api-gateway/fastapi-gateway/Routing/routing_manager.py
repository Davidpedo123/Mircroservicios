from fastapi import APIRouter, Depends, Request
from service_example import hellowork 
import httpx
  # Importa la lógica del login
from fastapi import Depends

manager_routing = APIRouter()

# Define la ruta para el login
@manager_routing.get("/service1")
def service1(request: Request):
    return hellowork()
