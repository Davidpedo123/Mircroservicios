# middleware/rate_limit.py
from fastapi import Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address

# Inicializa el limitador
limiter = Limiter(key_func=get_remote_address)

class RateLimitMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Crea un Request a partir del scope
        request = Request(scope, receive)
        
        # Aplica el limitador a cada solicitud
        response = limiter.check(request)

        if response is None:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        await self.app(scope, receive, send)
# Aplicar el límite global de 100 solicitudes por minuto
limiter.limit("5/minute")
