# fastapi-gateway/routes/api.py
from fastapi import APIRouter, FastAPI, Request
from routes.auth.auth_routes import router_auth as auth
from routes.users.users_routes import router_users as users
from routes.products.products_routes import router_product as products
from routes.service.routing_manager import manager_routing as service1

router = APIRouter()

#services = FastAPI()


#@services.get("/services1")
##async def service1()

# Incluir los routers de otras rutas
router.include_router(auth, prefix="/auth", tags=["auth"])
router.include_router(users, prefix="/user", tags=["user"])
router.include_router(products, prefix="/products", tags=["products"])
router.include_router(service1, prefix="/service", tags=["service"])

