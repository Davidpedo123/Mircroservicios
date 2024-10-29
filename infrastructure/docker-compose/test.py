import requests

# Definición de URLs y encabezados
url_auth = 'https://localhost/auth/token'
url_monto = 'https://localhost/user/monto'
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

# Prueba de autenticación
try:
    response = requests.post(url_auth, headers=headers_auth, data=data_auth, verify=False)
    response.raise_for_status()  # Lanza un error si la respuesta tiene un código de estado 4xx o 5xx
    content = response.json()
    
    if "access_token" in content:
        test_auth = True
    print(f"Resultado de la prueba de autenticación: {test_auth}")

except requests.exceptions.RequestException as e:
    print(f"Error en la prueba de autenticación: {e}")

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
    try:
        response = requests.get(url_monto, headers=headers_autorizacion, verify=False)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        content = response.json()
        
        if "dinero" in content:
            test_autorizacion = True
        print(f"Resultado de la prueba de autorización: {test_autorizacion}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la prueba de autorización: {e}")

print("Prueba de Authorization finalizada")


import sys

if test_auth and test_autorizacion:
    sys.exit(0)  # Exit with success
else:
    sys.exit(1)  # Exit with failure
