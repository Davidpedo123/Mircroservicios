from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from routes.api import router as api_router
#from middleware.https import RedirectHTTPToHTTPSMiddleware
from error.not_found import http_exception_handler as not_found
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
"""
Middleware
"""
#from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
#from fastapi.middleware.trustedhost import TrustedHostMiddleware
#from middleware.rate_limit import RateLimitMiddleware, limiter
#from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware

"""
CACHE
"""
#from routes.cache.cache_manager import CacheMiddleware as cache
import uvicorn

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="API Gateway")
"""
EL ORDEN DE LOS MIDDLEWARE ES CRUCIAL

"""

# app.add_middleware(RateLimitMiddleware)


#app.add_middleware(cache)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests. Please try again later."},
    )
#app.add_middleware(RedirectHTTPToHTTPSMiddleware)



#app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)



#app.state.limiter = limiter

#app.add_middleware(HTTPSRedirectMiddleware)

#app.add_middleware(RateLimitMiddleware)
#app.add_middleware(
#    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
#)



app.include_router(api_router)

#app.add_exception_handler(HTTPException, not_found)

@app.get("/")
#@limiter.limit("3/minute")
async def main(request: Request):
    return {"Welcome": "The api gateway"}

if __name__ == "__main__":
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=80
    )
