from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class CacheMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.cache = {}

    async def dispatch(self, request: Request, call_next):
        cache_key = request.url.path
        
        # Verificar si la respuesta está en caché
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Llamar al siguiente middleware o al controlador
        response = await call_next(request)

        # Almacenar la respuesta en caché
        self.cache[cache_key] = response

        # Modificar los encabezados después de la respuesta
        response.headers["Cache-Control"] = "max-age=15"

        return response