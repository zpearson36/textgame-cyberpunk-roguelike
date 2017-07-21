from items import Item

class Armour(Item):
    def __init__(self, name='', weight=0, value=0, aRating = 0, armClass=None):
        super().__init__(name=name, weight = weight, value = value, itemType="Armour")
        self._rating = aRating
        self._aClass = armClass

    def getRating(self):
        return self._rating

    def getArmourClass(self):
        return self._aClass
