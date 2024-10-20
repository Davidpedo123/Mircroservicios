FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /code
RUN ls -la /code
# Copiar el archivo requirements.txt desde la carpeta lib (subir un nivel)


COPY ../lib/requirements.txt /code/requirements.txt




# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY . /code/
