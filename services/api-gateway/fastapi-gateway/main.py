from fastapi import FastAPI, Request
from routes.api import router as api_router
import uvicorn

app = FastAPI(title="API Gateway")

# Incluir el router que contiene todas las rutas
app.include_router(api_router)

@app.get("/")
async def main(request:Request):
	return {"Welcome":"The api gateway"}

if __name__ == "__main__":
    # Ejecutar el servidor con Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
