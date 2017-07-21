import os
import threading
import time
import characters
class Game:
    def __init__(self):
        self._running = True

    def exit(self):
        print("Exiting...")
        raise SystemExit

    @classmethod
    def startThread(cls, listDisplay):
        t = threading.Thread(target=Game.rudimentaryDisplay, args=(listDisplay,))
        t.daemon = True
        t.start()

    @classmethod
    def rudimentaryDisplay(cls, listDisplay):
        while True:
            os.system('cls')
            for char in listDisplay:
                char.getLock().acquire()
                print("%s: %d -- %f"%(char.getName(), char.getHealth(), char.getAP()))
                char.getLock().release()
            time.sleep(.5)
