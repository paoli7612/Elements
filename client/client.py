import socket, time, threading

class Client:
    def __init__(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start("localhost")

    def start(self, ip, port=7612):
        connected = False
        while not connected:
            try:
                self.sock.connect((ip, port))
                connected = True
            except ConnectionRefusedError:
                print("Connessione non riuscita. Nuovo tentativo in corso...")
                time.sleep(0.5)

    def recv_all(self):
        while self.running:
            try:
                data = self.sock.recv(1024)
                message = data.decode()
                print(message)
            except ConnectionResetError:
                print("Connessione con il server persa")
                self.running = False


if __name__ == "__main__":
    c = Client()
    c.recv_all()
