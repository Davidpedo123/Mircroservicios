from fastapi import FastAPI, Request
from routes.api import router as api_router
#from middleware.https import RedirectHTTPToHTTPSMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
"""
Middleware
"""
#from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
#from fastapi.middleware.trustedhost import TrustedHostMiddleware
#from middleware.rate_limit import RateLimitMiddleware, limiter
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="API Gateway")


#app.add_middleware(RedirectHTTPToHTTPSMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)


#app.state.limiter = limiter

app.add_middleware(HTTPSRedirectMiddleware)

#app.add_middleware(RateLimitMiddleware)
#app.add_middleware(
#    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
#)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.include_router(api_router)

@app.get("/")
#@limiter.limit("3/minute")
async def main(request: Request):
    return {"Welcome": "The api gateway"}

if __name__ == "__main__":
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=443, 
        ssl_keyfile='./ssl/key.pem', 
        ssl_certfile='./ssl/cert.pem'
    )
