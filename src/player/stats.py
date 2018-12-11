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
    def __init__(self, d):
        self.life = Count(d["life"])
        self.mana = Count(d["mana"])

        self.attack = Attribute(d["attack"])
        self.defense = Attribute(d["defense"])
        self.speed = Attribute(d["speed"])
        self.range = Attribute(d["range"])
