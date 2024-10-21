


class RoundRobin:
    def __init__(self, servers):
        self.servers = servers
        self.counter = 0  # Inicializa el contador

    def get_next_server(self):
        # Obtiene el servidor actual basado en el contador
        selected_server = self.servers[self.counter]

        # Incrementa el contador
        self.counter += 1
        
        # Reinicia el contador si ha superado el número de servidores
        if self.counter >= len(self.servers):
            self.counter = 0
            
        return selected_server
