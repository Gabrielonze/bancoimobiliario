from random import randint

class Property(object):
    def __init__(self):
        self.price = randint(150, 250)
        self.rent = int(self.price * (randint(1, 9) / 10))
        self.owner = None

    def buy(self, newOwner):
        if (self.owner == None):
            self.owner = newOwner
