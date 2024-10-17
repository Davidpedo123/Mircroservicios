# fastapi-gateway/routes/api.py
from fastapi import APIRouter
from .auth import router as auth_router
from .users import router as users_router
from .products import router as products_router

# Crear el objeto APIRouter
router = APIRouter()

# Incluir los routers de otras rutas
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(products_router, prefix="/products", tags=["products"])
