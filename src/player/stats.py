import random
class Count:
    def __init__(self, v):
        self.value = v
        self.max = v
    def add(self, v):
        self.value += v
        self.value = min(self.value, self.max)
        if self.value <= 0:
            pass
    def __str__(self):
        return "%s/%s" %(self.value,self.max)

class Attribute:
    def __init__(self, v):
        self.value = v
    def add(self, v):
        self.value += v
        self.value = max(0, self.vlaue)
    def __str__(self):
        return "%s" %self.value

class Stats:
    def __init__(self):
        self.life = Count(10)
        self.mana = Count(10)

        self.attack = Attribute(10)
        self.defense = Attribute(10)
        self.speed = Attribute(random.randint(2,8))
        self.range = Attribute(3)
