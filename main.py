import player
import characters
import game
import locations

def interface(location):
    while location.getPlayer().isAlive() and any(location.inhabList()):
        for char in location.inhabList()+[location.getPlayer()]:
            if not char.isAlive(): continue
            elif char.isPlayer(): char.getAction()
            else: char.hit(location.getPlayer())
    print("Done!")

if __name__ == "__main__":
    location = locations.Location()
    character = characters.Character("Steve", location)
    char2 = characters.Character("Mitch", location)
    player = player.Player("Jim", location)
    location.addPlayer(player)
    location.addInhab(character)
    location.addInhab(char2)
    interface(location)
