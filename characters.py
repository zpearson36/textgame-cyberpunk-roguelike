from game import Game
from rng import Dice

class Character(Game):

    def __init__(self, name, location, attr = None):
        if attr == None: self._attr = {'str': 1, 'con': 1, 'agi': 1}
        else: self._attr = attr
        self._name = name
        self._health = self.MaxHealth()
        self._alive = True
        self._isPlayer = False
        self._location = location

    def getAttr(self, specAttr):
        return self._attr[specAttr]

    def getAttrMod(self, specAttr):
        return int(self._attr[specAttr]/3)

    def setAttr(self, specAttr, val):
        self._attr[specAttr] = val

    def MaxHealth(self):
        return 3+self.getAttrMod('con')

    def getLoc(self):
        return self._location

    def isPlayer(self):
        return self._isPlayer

    def isAlive(self):
        return self._alive

    def getName(self):
        return self._name

    def decrHealth(self, ammount = 1):
        self._health -= ammount
        print("%s: %d" % (self._name, self._health))
        if self._health <= 0:
            self._alive = False

    def hit(self, target):
        selfRoll = Dice.roll(20,1) + self.getAttrMod('agi')
        oppRoll = Dice.roll(20,1) + target.getAttrMod('agi')
        if selfRoll >= oppRoll:
            dmg = 1+self.getAttrMod('str')
            print("%s hits %s for %d point(s) of damage" % (self.getName(), target.getName(), dmg))
            target.decrHealth(dmg)
        else: print("%s misses %s" % (self.getName(), target.getName()))

    def __bool__(self):
        return self._alive
