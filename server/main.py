import time, random
from server import Server
from window import Window

def main(argv):
    try:
        port = int(argv[1])
    except:
        print("required [port]")
        exit(0)

    s = Server(port, 2)
    time.sleep(3)
    Window()
    time.sleep(3)
    print("window")

if __name__ == "__main__":
    import sys
    main(sys.argv)
    time.sleep(4)
