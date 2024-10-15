from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/hellowork")  
async def hellowork(request: Request):
    return {"Hello": "Work 2"}
