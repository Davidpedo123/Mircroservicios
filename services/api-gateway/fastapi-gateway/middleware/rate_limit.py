
from fastapi import Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)

class RateLimitMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
       
        request = Request(scope, receive)
        
        
        response = limiter.check(request)

        if response is None:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        await self.app(scope, receive, send)

limiter.limit("5/minute")
