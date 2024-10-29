Este repositorio consiste en una maqueta para el inicio de cualquier proyecto, la diferencia de este es que esta enfocado en que el dev se concentre totalmente en la logica del servicio, obviando la creaccion de APIs Gateway desde cero o el despliegue del proyecto.

Este proyecto esta dividido en dos carpetas importante que son:

`Infraestructure`: Aqui encontrara todo lo relacionado a la infraestructura, actualmente hay una maqueta para orquestacion de contenedores mediante docker compose y kubernetes, en el caso del docker compose posee un script en py, que le permite la creaccion del archivo de compose, solamente respondiendo las preguntas, en caso de que se desconozca la sintaxis de estos archivos.

![image](https://i.ibb.co/vBBpc14/general.jpg)

`Services`: Aqui tendremos nuestros servicios, cada servicio podria ser una aplicacion diferente, tambien poseeremos las `APIs Gateway`, hasta ahora posemos una en nginx y otra en fastapi, con funcionales estandar que posee una API Gateway como son, enrutamiento, balanceo de carga, auth y autorizacion etc.
La idea es que el dev solo cree un servicio nuevo en el cual aqui se encuentre toda su aplicacion , posterior decidir con que tecnologia desea desplegar sus servicios sea docker-compose o kubernetes ya luego que cree sus archivos de configuracion y defina los nombres de sus servicios solo tendrian que acceder a alguna `API Gateway` y modificar el apartado encargado de los upstream, y especificar el nombre del servicios al cual la API hara de proxi.

![image1](https://i.ibb.co/Jr4gTPp/componentes.jpg)

