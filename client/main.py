from client import Client

def main(argv):
    self.client = Client()
    self.client.start("127.0.0.1", 7612)

if __name__ == "__main__":
    import sys
    main(sys.argv)
