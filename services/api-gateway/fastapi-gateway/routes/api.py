# fastapi-gateway/routes/api.py
from fastapi import APIRouter
from routes.auth.auth_routes import router_auth as auth
from routes.users.users_routes import router_users as users
from routes.products.products_routes import router_product as products

# Crear el objeto APIRouter
router = APIRouter()

# Incluir los routers de otras rutas
router.include_router(auth, prefix="/auth", tags=["auth"])
router.include_router(users, prefix="/user", tags=["user"])
router.include_router(products, prefix="/products", tags=["products"])

