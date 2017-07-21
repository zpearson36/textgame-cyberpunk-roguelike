import player
import characters
import game
import locations

def interface(location):
    while all(location.inhabList()):
        for char in location.inhabList():
            if char.isAlive():
                if char.isPlayer():
                    exitLoop = False
                    while not exitLoop:
                        exitLoop = char.getAction()
                        
                else:
                    char.hit(location.getPlayer())
    print("Done!")

if __name__ == "__main__":
    character = characters.Character("Steve")
    location = locations.Location(character)
    player = player.Player("Jim", location)
    location.addPlayer(player)
    interface(location)
