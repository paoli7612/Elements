from match import Match

class Boss:
    def __init__(self):
        self.match = Match()

def main(argv):
    b = Boss()

if __name__ == "__main__":
    import sys
    main(sys.argv)
