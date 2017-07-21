from characters import Character
import locations

class Player(Character):

    def __init__(self, name, location):
        Character.__init__(self, name, location)
        self._isPlayer = True

    def getAction(self):
        stopLoop = False
        while not stopLoop:
            act = input().split()
            if len(act) > 1: arg = act[1]
            else: arg = ''
            try:
                method = getattr(self,act[0])
                stopLoop = True
            except AttributeError:
                print("Not a valid action")
        method(arg)


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
        super(Player, self).hit(target)
