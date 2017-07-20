import player
import characters
import game
import locations

def interface(player, *args):
    while True:
        player.getAction()
        for arg in args:
            arg.hit(player)

if __name__ == "__main__":
    character = characters.Character("Steve")
    location = locations.Location(character)
    player = player.Player("Jim", location)
    location.addPlayer(player)
    interface(player, character)
