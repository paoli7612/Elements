import socket, time

class Client:
    def __init__(self):
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


if __name__ == "__main__":
    c = Client()
