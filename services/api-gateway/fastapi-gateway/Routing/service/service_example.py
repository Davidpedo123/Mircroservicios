from fastapi import FastAPI, HTTPException
import httpx


async def hellowork():
    url = "http://api:8050"  # Cambia esto por la URL de tu servicio interno
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Lanza un error si la respuesta no es 2xx
            return response.json()  # Devuelve la respuesta como JSON
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))