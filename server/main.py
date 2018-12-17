from server import Server

def main(argv):
    s = Server()
    s.start()
    s.wait_clients(1)

if __name__ == "__main__":
    import sys
    main(sys.argv)
