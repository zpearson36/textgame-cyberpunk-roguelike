import threading

class Dialogue:

    @classmethod
    def converse(cls, player, npc):
        player.getLock().acquire()
        npc.getLock().acquire()
        npc.greeting()
        response = input()
        while response != "done":
            response = input()
        player.getLock().release()
        npc.getLock().release()
