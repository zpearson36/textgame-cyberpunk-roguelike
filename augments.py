from items import Item

class Augment(Item):
    def __init__(self, name='', mod=None, augClass=None, value=0):
        super().__init__(name, itemType="Augment", value=value)
        self._augClass = augClass
        if mod==None: self._modifiers = {'str': 0, 'con': 0, 'agi': 0}
        else: self._modifiers = mod

    def getAugClass(self):
        return self._augClass

    def getModifiers(self):
        return self._modifiers
