import time
from client import Client

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        print("required [ip] [port]")
        exit(0)

    client = Client()
    client.start(host, port)

if __name__ == "__main__":
    import sys
    main(sys.argv)
    time.sleep(5)
