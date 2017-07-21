import player
import characters
import game
import locations
import weapons
import armour
def interface(location):
    while location.getPlayer().isAlive() and any(location.inhabList()):
        for char in location.inhabList()+[location.getPlayer()]:
            if not char.isAlive(): continue
            char.getAction()
    print("Done!")

if __name__ == "__main__":
    location = locations.Location()
    character = characters.Character("Steve", location)
    char2 = characters.Character("Mitch", location)
    player = player.Player("Jim", location)
    location.addPlayer(player)
    location.addInhab(character)
    location.addInhab(char2)
    stick = weapons.Weapon(name="stick", damage={'sides':4,'num':2})
    jerkin = armour.Armour(name="jerkin", aRating = 2, aClass = "torso")
    player.equip(stick)
    player.equip(jerkin)
    interface(location)
