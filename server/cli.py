from cmd import Cmd
from server import Server

class Cli(Cmd):
    do_quit = lambda _,__:True
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.server = Server()
        self.cmdloop()

    def do_show(self, args):
        self.server.users.show()

    def do_sendall(self, args):
        self.server.send_all(args)

if __name__ == "__main__":
    c = Cli()
    c.run()
