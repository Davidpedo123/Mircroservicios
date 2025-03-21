from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

async def rate_limit_exceeded(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "message": "Too Many Requests",
            "error": {
                "detail": str(exc),  
                "allowed": exc.allowed,  
                "retry_after": exc.retry_after,  
            },
        },
    )
