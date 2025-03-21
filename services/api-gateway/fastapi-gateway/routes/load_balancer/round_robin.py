


class RoundRobin:
    def __init__(self, servers):
        self.servers = servers
        self.counter = 0 

    def get_next_server(self):
        
        selected_server = self.servers[self.counter]

        
        self.counter += 1
        
        
        if self.counter >= len(self.servers):
            self.counter = 0
            
        return selected_server
