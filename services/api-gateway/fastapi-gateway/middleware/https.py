from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class RedirectHTTPToHTTPSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        if request.url.scheme == "http":
            
            https_url = request.url.replace(scheme="https")
            return Response(status_code=301, headers={"Location": str(https_url)})
        
        
        response = await call_next(request)
        return response




