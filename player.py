from characters import Character
import locations

class Player(Character):

    def __init__(self, name, location):
        Character.__init__(self, name)
        self._location = location

    def getAction(self):
        act = input("What DO").split()
        try:
            method = getattr(self,act[0])
        except AttributeError:
            print("Not a valid action")
            return False
        method()
        return True

    def getLoc(self):
        return self._location

    def hit(self, name = ''):
        if name == '':
            print('Who would you like to hit?')
            self.getLoc().listInhabs()
            stopLoop = False
            while not stopLoop:
                targetName = input().lower()
                target = self.getLoc().getInhab(targetName)
                if target != "N/A": stopLoop = True
            super(Player, self).hit(target)
