class User:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def __str__(self):
        return "User %s" %str(self.addr)

    def send(self, message):
        data = message.encode()
        self.conn.send(data)

class Users:
    def __init__(self):
        self.data = list()

    def __iter__(self):
        return self.data.__iter__()

    def new(self, conn, addr):
        user = User(conn, addr)
        self.data.append(user)

    def show(self):
        for user in self.data:
            print(user)

    def send_all(self, message):
        for user in self:
            user.send(message)
