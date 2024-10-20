from fastapi import FastAPI, Request
from routes.api import router as api_router, services 
import uvicorn

app = FastAPI(title="API Gateway")

# Incluir el router que contiene todas las rutas
app.include_router(api_router)

@app.get("/")
async def main(request: Request):
    return {"Welcome": "The api gateway"}

if __name__ == "__main__":
    # Ejecutar el servidor con Uvicorn utilizando SSL
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=443, 
        ssl_keyfile='./ssl/key.pem', 
        ssl_certfile='./ssl/cert.pem'
    )
