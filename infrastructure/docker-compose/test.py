import requests
import time
import sys

# Definición de URLs y encabezados
url_auth = 'http://localhost:80/auth/token'
url_monto = 'http://localhost:80/user/monto'
headers_auth = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data_auth = {
    'grant_type': 'password',
    'username': 'user1',
    'password': 'password1',
    'scope': '',
    'client_id': 'string',
    'client_secret': 'string'
}

# Variables para seguimiento de las pruebas
test_auth = False
test_autorizacion = False

# Configuración de reintentos
max_retries = 5  # Número máximo de reintentos
retry_delay = 5  # Tiempo de espera entre reintentos (en segundos)

# Función para realizar una solicitud POST con reintentos
def request_with_retries(method, url, headers=None, data=None):
    for attempt in range(max_retries):
        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=data, verify=False)
            elif method == 'GET':
                response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()  # Lanza un error si la respuesta tiene un código de estado 4xx o 5xx
            return response  # Si la solicitud fue exitosa, devuelve la respuesta
        except requests.exceptions.RequestException as e:
            print(f"Intento {attempt + 1} fallido: {e}")
            if attempt < max_retries - 1:  # Si no es el último intento
                print(f"Reintentando en {retry_delay} segundos...")
                time.sleep(retry_delay)  # Espera antes de reintentar

    return None  # Devuelve None si todos los intentos fallan

# Prueba de autenticación
response = request_with_retries('POST', url_auth, headers=headers_auth, data=data_auth)

if response is not None:
    content = response.json()
    if "access_token" in content:
        test_auth = True
    print(f"Resultado de la prueba de autenticación: {test_auth}")
else:
    print("Error: No se pudo completar la autenticación después de múltiples intentos.")

print("Prueba de auth finalizada")

# Si la autenticación fue exitosa, procede con la autorización
if test_auth:
    token = content.get("access_token")  # Usa get para evitar KeyError
    token_type = content.get("token_type")

    headers_autorizacion = {
        'accept': 'application/json',
        'Authorization': f'{token_type} {token}'
    }

    # Prueba de autorización
    response = request_with_retries('GET', url_monto, headers=headers_autorizacion)

    if response is not None:
        content = response.json()
        if "dinero" in content:
            test_autorizacion = True
        print(f"Resultado de la prueba de autorización: {test_autorizacion}")
    else:
        print("Error: No se pudo completar la autorización después de múltiples intentos.")

print("Prueba de Authorization finalizada")

# Salida según los resultados de las pruebas
if test_auth and test_autorizacion:
    sys.exit(0)  # Exit with success
else:
    sys.exit(1)  # Exit with failure
