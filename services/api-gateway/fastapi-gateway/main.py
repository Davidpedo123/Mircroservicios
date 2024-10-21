from fastapi import FastAPI, Request
from routes.api import router as api_router, services 
from middleware.https import RedirectHTTPToHTTPSMiddleware
import uvicorn

app = FastAPI(title="API Gateway")
#app.add_middleware(RedirectHTTPToHTTPSMiddleware)

app.include_router(api_router)

@app.get("/")
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
