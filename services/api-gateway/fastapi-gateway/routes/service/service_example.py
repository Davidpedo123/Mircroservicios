from fastapi import FastAPI, HTTPException
import httpx
from ..load_balancer.round_robin import RoundRobin


servers = ["http://api:8050", "http://api2:8050"]  # Asegúrate de que las URLs sean correctas
rr = RoundRobin(servers)

async def hellowork():
    # Obtiene el siguiente servidor usando el algoritmo Round Robin
    url = rr.get_next_server() + "/hellowork"  # Construye la URL del servicio
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Lanza un error si la respuesta no es 2xx
            return response.json()  # Devuelve la respuesta como JSON
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))