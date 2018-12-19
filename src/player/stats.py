import random
class Count:
    def __init__(self, s, v):
        self.stats = s
        self.value = v
        self.max = v
    def add(self, v):
        self.value += v
        self.value = min(self.value, self.max)
        if self.value <= 0:
            self.stats.live = False

    def neg(self, v):
        return self.add(-v)
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
    def __init__(self, d):
        self.live = True
        self.life = Count(self,d["life"])
        self.mana = Count(self,d["mana"])

        self.attack = Attribute(d["attack"])
        self.defense = Attribute(d["defense"])
        self.speed = Attribute(d["speed"])
        self.range = Attribute(d["range"])
