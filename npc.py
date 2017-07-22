from characters import Character
import time
class NPC(Character):

    def __init__(self, name, location, attr = None, armour = None, weapon = None, augments = None, statMods = None, disposition=None, hostile = False):
        super().__init__(name=name, location=location, attr = attr, armour = armour, weapon = weapon, augments = augments, statMods = statMods)
        if disposition == None: self._disposition = {'Player': 50}
        else: self._disposition = disposition
        self._hostile = hostile

    def getDisposition(self, name):
        return self._disposition[name]

    def updateDisposition(self, name, val):
        self._disposition[name] += val
        if self._disposition[name] > 100: self._disposition[name] = 100
        if self._disposition[name] < 0: self._disposition[name] = 0
        if self._disposition[name] < 20: self.setHostile(True)

    def isHostile(self):
        return self._hostile

    def setHostile(self, val):
        self._hostile = val

    def getAction(self):
        while self.isAlive() and self.getLoc().getPlayer().isAlive():
            if self.isHostile(): self.hit(self.getLoc().getPlayer())
            time.sleep(.5)
            self.replenishAP()

    def greeting(self):
        print("Hello, my name is %s" % (self.getName()))
