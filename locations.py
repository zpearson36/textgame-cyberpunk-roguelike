import characters

class Location:

    def __init__(self, *chars):
        self._inhabs = {}
        for character in chars:
            self._inhabs[character.getName().lower()] = character

    def addInhab(self, character):
        self._inhabs[character.getName().lower()] = character

    def addPlayer(self, player):
        self._player = player

    def getPlayer(self):
        return self._player

    def getInhab(self, name):
        if name in self._inhabs:
            return self._inhabs[name]
        else:
            print("No such inhabitant")
            return "N/A"

    def displayInhabs(self):
        for char in list(self._inhabs.keys()):
            if char != "Player": print(char)

    def inhabList(self):
        return list(self._inhabs.values())
