from game import Game
from rng import Dice
import weapons
import time
import threading

class Character(Game):

    def __init__(self, name, location, attr = None, armour = None, weapon = None, augments = None, statMods = None):
        if attr == None: self._attr = {'str': 5, 'con': 5, 'agi': 5}
        else: self._attr = attr
        if armour == None: self._armour = {'head': None, 'torso': None, 'legs': None}
        else: self._armour = armour
        if augments == None: self._augments = {'muscle': None, 'cognitive': None, 'Bone': None, 'metabolic': None}
        else: self.augments = augments
        if statMods == None: self._statMods = {'str': 0, 'con': 0, 'agi': 0}
        else: self._statMods = statMods
        self._actPoints = self.maxActPoints()
        self._weapon = weapon
        self._name = name
        self._health = self.MaxHealth()
        self._alive = True
        self._isPlayer = False
        self._location = location
        self._lock = threading.Lock()
        self._thread = None

    def maxActPoints(self):
        return 5 + self.getAttrMod('agi')*(1.5)

    def replenishAP(self):
        self._actPoints += .1*self.getAttr('agi')
        if self._actPoints > self.maxActPoints(): self._actPoints = self.maxActPoints()

    def reduceAP(self, val):
        self._actPoints -= val

    def getAP(self):
        return self._actPoints

    def getAttr(self, specAttr):
        return self._attr[specAttr] + self._statMods[specAttr]

    def getAttrMod(self, specAttr):
        return int((self._attr[specAttr] + self._statMods[specAttr])/2) - 2

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
        itemType = item.getType()
        if itemType == "Weapon":
            if self._weapon != None: self.unequip(self._weapon)
            self._weapon = item
        elif itemType == "Armour":
            if self._armour[item.getArmourClass()] != None: self.unequip(self._armour[item.getArmourClass()])
            self._armour[item.getArmourClass()] = item
        elif itemType == "Augment":
            if self._augments[item.getAugClass()] != None: self.unequip(self._augments[item.getAugClass()])
            self._augments[item.getAugClass()] = item
            self.addModifiers(item.getModifiers())
        else: print("Cannot Equip")

    def addModifiers(self, modifiers):
        for stat in list(self._statMods.keys()):
            self._statMods[stat] += modifiers[stat]

    def unequip(self, item):
        itemType = item.getType()
        if itemType == "Weapon":
            self._weapon = None
        elif itemType == "Armour":
            self._armour[item.getArmourClass()] = None
        elif itemType == "Augment":
            self._augments[item.getAugClass()] = None
            self.removeModifiers(item.getModifiers())
        else: print("No such equipment")

    def removeModifiers(self, modifiers):
        for stat in list(self._statMods.keys()):
            self._statMods[stat] -= modifiers[stat]

    def getLoc(self):
        return self._location

    def isPlayer(self):
        return self._isPlayer

    def isAlive(self):
        return self._alive

    def getName(self):
        return self._name

    def getHealth(self):
        return self._health

    def decrHealth(self, ammount = 1):
        self._health -= ammount
        print("%s: %d" % (self._name, self._health))
        if self._health <= 0:
            self._alive = False

    def getLock(self):
        return self._lock

    def startThread(self):
        self._thread = threading.Thread(target=self.getAction, name=self.getName())
        self._thread.start()

    def getThread(self):
        return self._thread

    def getAction(self):
        while self.isAlive() and self.getLoc().getPlayer().isAlive():
            self.hit(self.getLoc().getPlayer())
            time.sleep(.5)
            self.replenishAP()

    def getDmg(self):
        if self._weapon == None: return 1+self.getAttrMod('str')
        else: return self._weapon.getDamage(self)

    def hit(self, target):
        dmg = 0
        if self._actPoints >= 2:
            target.getLock().acquire()
            self.reduceAP(2)
            selfRoll = Dice.roll(20,1) + self.getAttrMod('agi')
            oppRoll = Dice.roll(20,1) + target.getAttrMod('agi')
            if selfRoll >= oppRoll:
                dmg = self.getDmg() - target.getArmourRating()
                if dmg < 0: dmg = 0
                print("%s hits %s for %d point(s) of damage" % (self.getName(), target.getName(), dmg))
                target.decrHealth(dmg)
            else: print("%s misses %s" % (self.getName(), target.getName()))
            target.getLock().release()
        return dmg

    def __bool__(self):
        return self._alive
