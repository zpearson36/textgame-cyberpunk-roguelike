import player
import characters
from game import Game
import locations
import weapons
import armour
import augments
import threading
import npc
import time

def interface(location):
    for char in location.inhabList()+[location.getPlayer()]:
        if not char.isAlive(): continue
        char.startThread()
    #Game.startThread(location.inhabList()+[location.getPlayer()]) #allows for rudimentary Display - buggy
    while location.getPlayer().isAlive() and any(location.inhabList()):
        pass

    for char in location.inhabList()+[location.getPlayer()]:
        char._alive = False

    print("Done!")

if __name__ == "__main__":
    location = locations.Location()
    character = npc.NPC("Steve", location)
    char2 = npc.NPC("Mitch", location)
    player = player.Player("Jim", location)
    location.addPlayer(player)
    location.addInhab(character)
    location.addInhab(char2)
    #stick = weapons.Weapon(name="stick", damage={'sides':4,'num':2})
    jerkin = armour.Armour(name="jerkin", aRating = 20, armClass = "torso")
    #roboArm = augments.Augment(name="Robotic Arm", mod={'str': 500, 'agi':500, 'con': 0}, augClass='muscle')
    #player.equip(stick)
    player.equip(jerkin)
    #player.equip(roboArm)
    interface(location)
