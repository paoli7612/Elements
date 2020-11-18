import socket, time, threading

class Client:
    def __init__(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, ip, port):
        connected = False
        timeout = 0
        while not connected:
            try:
                self.sock.connect((ip, port))
                connected = True
            except ConnectionRefusedError:
                print("Connessione non riuscita. Nuovo tentativo in corso...")
                time.sleep(0.5)
                timeout += 1
            if (timeout > 5):
                print("Time out")
                exit(0)

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
