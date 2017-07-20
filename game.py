class Game:
    def __init__(self):
        self.running = True

    def exit(self):
        print("Exiting...")
        raise SystemExit
