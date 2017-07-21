from game import Game
from rng import Dice
import weapons

class Character(Game):

    def __init__(self, name, location, attr = None, armour = None, weapon = None):
        if attr == None: self._attr = {'str': 3, 'con': 3, 'agi': 3}
        else: self._attr = attr
        if armour == None: self._armour = {'head': None, 'torso': None, 'legs': None}
        else: self._armour = armour
        self._weapon = weapon
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

    def getArmourRating(self):
        defense = 0
        for armour in list(self._armour.values()):
            if armour == None:
                defense += 0
            else:
                defense += armour.getRating()
        return defense

    def equip(self, item):
        if item.getType() == "Weapon": self._weapon = item
        elif item.getType() == "Armour": self._armour[item.getArmourClass()] = item
        else: print("Cannot Equip")

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

    def getAction(self):
        self.hit(self.getLoc().getPlayer())

    def getDmg(self):
        if self._weapon == None: return 1+self.getAttrMod('str')
        else: return self._weapon.getDamage(self)

    def hit(self, target):
        selfRoll = Dice.roll(20,1) + self.getAttrMod('agi')
        oppRoll = Dice.roll(20,1) + target.getAttrMod('agi')
        if selfRoll >= oppRoll:
            dmg = self.getDmg() - target.getArmourRating()
            if dmg < 0: dmg = 0
            print("%s hits %s for %d point(s) of damage" % (self.getName(), target.getName(), dmg))
            target.decrHealth(dmg)
        else: print("%s misses %s" % (self.getName(), target.getName()))

    def __bool__(self):
        return self._alive
