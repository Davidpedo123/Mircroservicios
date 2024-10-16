#Docker Compose

Con docker compose podremos orquestar nuestros contenedores, de la siguiente manera:

1-`Creamos los servicios a usar`: en el modelo actual los servicios, que se alojaran en la carpeta `Microservicios/services/` alojaremos lo que es la logica de nuestra aplicacion, en el modelo actual, tenemos varios servicios que uno es una replica del otro, llamados `api-example y api-example2`.
en estas carpetas podemos modificarla a gusto, tanto el el dockerfile como el codigo fuente.

2-`Orquestacion`: luego de que hallamos agregado la logica de nuestro servicios, solo ajustariamos el archivo `docker-compose.yml` dependiendo de las necesidades de nuestro servicio y el ejecutar el comando `docker-compose up --build`.

En el modelo actual, se tiene una API Gateway que hace de enrutador, balanceador y permite la autenticacion, la tecnologia usada en este caso es nginx.

`nginx`: en el archivo `default` agregaremos la configuraciones de nuestros servidores, aqui configurar el enrutamiento o el balanceo.