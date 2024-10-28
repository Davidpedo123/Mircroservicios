import copy
import yaml
import os

class ServiceConfig:
    def __init__(self, name, image_type, context=None, dockerfile=None, tag=None, port_option=None, port=None, volume=None, network=None, command=None):
        self.name = name
        self.image_type = image_type
        self.context = context
        self.dockerfile = dockerfile
        self.tag = tag
        self.port_option = port_option  # Determina si usa "expose" o "ports"
        self.port = port
        self.volume = volume
        self.network = network
        self.command = command  # Nuevo atributo para el comando

    def to_dict(self):
        # Convierte el objeto ServiceConfig en un diccionario compatible con YAML
        service_dict = {}
        
        match self.image_type:
            case 's':  # Imagen ya creada
                service_dict['image'] = self.tag
            case 'n':  # Imagen construida mediante Dockerfile
                service_dict['build'] = {
                    'context': self.context,
                    'dockerfile': self.dockerfile
                }
        
        # Añadir el puerto según la opción seleccionada
        match self.port_option:
            case 's':  # Red interna
                service_dict['expose'] = [self.port]  # Se usa una lista
            case 'n':  # Red del host
                service_dict['ports'] = [self.port]  # Se usa una lista

        # Configura otros parámetros si están presentes
        if self.volume:
            service_dict['volumes'] = [self.volume]  # Se usa una lista
        if self.network:
            service_dict['networks'] = [self.network]  # Se usa una lista
        if self.command:  # Añadir el comando si está presente
            service_dict['command'] = self.command

        return service_dict

class ComposeConfig:
    def __init__(self, version):
        self.version = version
        self.services = {}

    def add_service(self, service):
        # Añade un nuevo servicio al archivo compose
        self.services[service.name] = service.to_dict()

    def to_dict(self):
        # Convierte toda la configuración a un diccionario compatible con YAML
        return {
            'version': self.version,
            'services': self.services
        }

    def to_yaml(self):
        # Serializa el diccionario como YAML usando PyYAML
        return yaml.dump(self.to_dict(), sort_keys=False, default_flow_style=False)

# Función para capturar datos de entrada del usuario
def get_service_config():
    services_name = str(input("Ingrese el nombre del servicio: "))
    image_type = str(input("¿Usará una imagen ya creada (s) o la construirá mediante un Dockerfile (n)? "))

    match image_type:
        case 's':
            tag = str(input("Ingrese el tag de la imagen: "))
            command = str(input("Ingrese el comando a ejecutar (dejar vacío si no se requiere): ")) or None
            return ServiceConfig(name=services_name, image_type=image_type, tag=tag, command=command)
        
        case 'n':
            context = str(input("Ingrese el contexto o la ruta base del proyecto: "))
            dockerfile = str(input("Ingrese la ruta del Dockerfile: "))
            port_option = str(input("¿Desea exponer el puerto en la red interna (s) o en la red del host (n)? "))
            port = str(input("Ingrese el puerto a exponer (ejemplo: '8080:80'): "))
            volume = str(input("Ingrese el volumen del proyecto (ejemplo: 'services/api-example/src:/code/api-example/src'): "))
            network = str(input("Ingrese el nombre de la red (ejemplo: 'app-network'): "))
            command = str(input("Ingrese el comando a ejecutar (dejar vacío si no se requiere): ")) or None
            return ServiceConfig(
                name=services_name,
                image_type=image_type,
                context=context,
                dockerfile=dockerfile,
                port_option=port_option,
                port=port,
                volume=volume,
                network=network,
                command=command  # Pasar el comando
            )

# Creación de archivo compose.yml
def create_compose():
    version = str(input("Ingrese la versión de Compose a utilizar: "))
    compose_config = ComposeConfig(version=version)

    # Añadir primer servicio
    service = get_service_config()
    compose_config.add_service(service)

    # Preguntar si se desea añadir otro servicio
    add_another = input("¿Desea añadir otro servicio similar? (s/n): ")
    while add_another.lower() == 's':
        # Crear un nuevo servicio con la misma estructura de preguntas
        new_service = get_service_config()
        compose_config.add_service(new_service)
        add_another = input("¿Desea añadir otro servicio similar? (s/n): ")

    # Generar el YAML y sobreescribir si ya existe
    file_path = "docker-compose.yml"
    if os.path.exists(file_path):
        print("El archivo docker-compose.yml ya existe y será sobrescrito.")
    with open(file_path, "w") as f:
        f.write(compose_config.to_yaml())
    print("Archivo docker-compose.yml creado exitosamente.")

# Ejecutar la función de creación de compose
create_compose()
