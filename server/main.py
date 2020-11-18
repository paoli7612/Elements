import time, random
from server import Server
from window import Window


def main(argv):
    try:
        port = int(argv[1])
    except:
        print("required [port]")
        exit(0)

    s = Server()
    s.start(port)
    s.wait_clients(2)

if __name__ == "__main__":
    import sys
    main(sys.argv)
    time.sleep(5)
