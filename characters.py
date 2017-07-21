from game import Game

class Character(Game):

    def __init__(self, name, location):
        self._name = name
        self._health = 5
        self._alive = True
        self._isPlayer = False
        self._location = location

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
        target.decrHealth(2)

    def __bool__(self):
        return self._alive
