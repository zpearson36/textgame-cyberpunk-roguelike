from items import Item
from rng import Dice

class Weapon(Item):
    def __init__(self, name='', weight = 0, value = 0, damage = None, ranged=False):
        super().__init__(name, itemType="Weapon", weight = weight, value = value)
        if damage == None: self._damage = {'sides': 0, 'num': 0}
        else: self._damage = damage
        self._ranged = ranged

    def isRanged(self):
        return self._ranged

    def getDamage(self, user):
        if self.isRanged: modifier = user.getAttrMod('agi')
        else: modifier = user.getAttrMod('str')
        return Dice.roll(self._damage['sides'], self._damage['num']) + modifier
