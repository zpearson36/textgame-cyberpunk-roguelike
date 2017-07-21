from random import randint
class Dice:

    @classmethod
    def roll(cls, sides, num):
        sum = 0
        for x in range(num):
            sum += randint(1, sides)

        return sum
