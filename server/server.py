import socket
from users import Users
class Server:
    def __init__(self, max_users=1):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = Users()
        self.start()
        self.wait_clients(max_users)

    def start(self, port=7612):
        try:
            self.sock.bind(("localhost", port))
            self.sock.listen(2)
        except OSError:
            print("Server gia avviato")
            self.running = False

    def wait_clients(self, max_users):
         for n in range(1, max_users+1):
            print("In attesa del client numero %d" %(n))
            sock = self.sock.accept()
            self.users.new(*sock)
            print("Client correttamente connesso")

    def show_users(self):
        for user in self.users():
            print(user)

    def send_all(self, message):
        self.users.send_all(message)
