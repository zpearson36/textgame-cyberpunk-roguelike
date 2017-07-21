class Items:
    def __init__(self, name='', itemType=None, weight = 0, value=0):
        self._name = name
        self._type = itemType
        self._weight = weight
        self._value = value

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getWeight(self):
        return self._weight

    def getValue(self):
        return self._value
