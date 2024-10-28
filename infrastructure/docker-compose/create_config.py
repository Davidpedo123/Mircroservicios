import copy
import yaml
import os
import sys
import subprocess
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(sequence=4, offset=2)

class ServiceConfig:
    def __init__(self, name, image_type, context=None, dockerfile=None, tag=None, port_option=None, port=None, volume=None, network=None, command=None):
        self.name = name
        self.image_type = image_type
        self.context = context
        self.dockerfile = dockerfile
        self.tag = tag
        self.port_option = port_option
        self.port = port
        self.volume = volume
        self.network = network
        self.command = command

    def to_dict(self):
        service_dict = {}
        
        match self.image_type:
            case 's':
                service_dict['image'] = self.tag
            case 'n':
                service_dict['build'] = {
                    'context': self.context,
                    'dockerfile': self.dockerfile
                }

        match self.port_option:
            case 's':
                service_dict['expose'] = [self.port]
            case 'n':
                service_dict['ports'] = [self.port]

        if self.volume:
            service_dict['volumes'] = [self.volume]
        if self.network:
            service_dict['networks'] = [self.network]
        if self.command:
            service_dict['command'] = self.command

        return service_dict

class ComposeConfig:
    def __init__(self, version):
        self.version = version
        self.services = {}
        self.networks = {}

    def add_service(self, service):
        self.services[service.name] = service.to_dict()
        if service.network:
            self.networks[service.network] = {
                'driver': 'bridge'
            }

    def to_dict(self):
        return {
            'version': self.version,
            'services': self.services,
            'networks': self.networks
        }

    def to_yaml(self):
        return yaml.dump(self.to_dict())

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
            network = str(input("Ingrese el nombre de la red (ejemplo: 'app-network', dejar vacío si no desea definir una red): ")) or None
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
                command=command
            )

def create_compose():
    version = str(input("Ingrese la versión de Compose a utilizar: "))
    compose_config = ComposeConfig(version=version)

    service = get_service_config()
    compose_config.add_service(service)

    add_another = input("¿Desea añadir otro servicio similar? (s/n): ")
    while add_another.lower() == 's':
        new_service = get_service_config()
        compose_config.add_service(new_service)
        add_another = input("¿Desea añadir otro servicio similar? (s/n): ")

    file_path = "docker-compose.yml"
    if os.path.exists(file_path):
        print("El archivo docker-compose.yml ya existe y será sobrescrito.")
    with open(file_path, "w") as f:
        yaml.dump(compose_config.to_dict(), f)

    print("Archivo docker-compose.yml creado exitosamente.")

    # Preguntar al usuario si desea ejecutar el compose
    run_compose = input("¿Desea ejecutar docker-compose up --build? (s/n): ")
    if run_compose.lower() == 's':
        try:
            result = subprocess.run(['docker-compose', 'up', '--build'], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error al ejecutar docker-compose:")
            print(e.output)  # Capturar el output del error
            print(f"Mensaje de error: {e.stderr}")  # Capturar el mensaje de error

# Ejecutar la función de creación de compose
create_compose()
