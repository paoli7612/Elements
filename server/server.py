import socket

class Server:
    def __init__(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = list()
        self.start()

    def start(self, port=7612):
        try:
            self.sock.bind(("localhost", port))
            self.sock.listen(2)
        except OSError:
            print("Server gia avviato")
            self.running = False

    def wait_clients(self, max_users):
         for n in range(max_users):
            user, client_address = self.sock.accept()
            print("Client correttamente connesso")
            self.users.append(user)

if __name__ == "__main__":
    s = Server()
    s.wait_clients(1)
