from fastapi import APIRouter, Depends, Request
from service_example import hellowork 
import httpx

from fastapi import Depends

manager_routing = APIRouter()


@manager_routing.get("/service1")
def service1(request: Request):
    return hellowork()
