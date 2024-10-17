from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

# Incluir el router que contiene todas las rutas
app.include_router(api_router)

@app.get("/")
async main(request:Request):
	return {"Welcome":"The api gateway"}


