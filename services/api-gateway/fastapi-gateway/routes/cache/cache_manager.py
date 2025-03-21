from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class CacheMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.cache = {}

    async def dispatch(self, request: Request, call_next):
        cache_key = request.url.path
        
        if cache_key in self.cache:
            return self.cache[cache_key]

        
        response = await call_next(request)

        
        self.cache[cache_key] = response

        
        response.headers["Cache-Control"] = "max-age=15"

        return response
