from characters import Character
import locations
import time
class Player(Character):

    def __init__(self, name, location, attr = None):
        super().__init__(name, location, attr)
        self._isPlayer = True

    def getAction(self):
        while self.isAlive():
            act = input().split()
            if len(act) > 1: arg = act[1]
            else: arg = ''
            if len(act) == 0: continue
            try:
                method = getattr(self,act[0])
                stopLoop = True
                if arg == '': method()
                else: method(arg)
            except AttributeError:
                print("Not a valid action")
            time.sleep(.5)
            self.replenishAP()

    def exit(self):
        print("Exiting...")
        for chars in self.getLoc().inhabList():
            chars._alive = False
        raise SystemExit


    def hit(self, name = ''):
        stopLoop = False
        while not stopLoop:
            if name == '':
                print('Who would you like to hit?')
                self.getLoc().displayInhabs()
                name = input().lower()
            target = self.getLoc().getInhab(name)
            if target != "N/A": stopLoop = True
            else: name = ''
        print(super().hit(target))
        target.updateDisposition('Player', -31*super().hit(target))
