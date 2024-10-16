
--Conocimientos Previos--
Docker
Docker-hub
Kubernetes-cluster

toke user dashboard
command `kubectl create token dashboard-admin -n kubernetes-dashboard`

Para implementar esta infraestructura se debe realizar diferentes pasos.

1-`Crear un cluster de kubernetes:` En el modelo actual solo es en local, se probo con el kubernetes que brinda docker desktop

2-`Crear las imagenes docker de nuestra app`: Por cada contenedor que necesite o servicio le creara una imagen, si toda su apliacion se puede ejecutar en una imagen, solo creara esa imagen

en el modelo de ejemplo, la imagen se creo apartir del servicio `services/api-example`

3-`Agregar tag y subir docker hub`: Dependiendo del registro que use, esto podria ser distinto, en el ejemplo actual se utilizo el registro de docker hub, primero la imagen que creamos anteriormente le agregamos el tag `username/repository`:`name-image:version` luego de que creamos el tag, hacemos el push, nota, anteriormente debemos tener un repositorio en docker hub y logearnos, mediante la terminal con `docker login`

4-`Crear el deployment`: en la ruta `deployment` agregaremos nuestros deployments, o modificamos el actual 

5-`Crear el service`: en la ruta `svc` agregaremos nuestros services (aqui configuraremos como se comunicaran nuestros pods), o modificamos el actual.

6-`Aplicamos los archivos de config`: el comando es `kubectl apply -f (namefile)` debe tener instalado kubectl

7-`Extras kubernetes dashboard`: Podemos hacer todo esto por una gui de kubernetes, llamado kubernetes dashboard.