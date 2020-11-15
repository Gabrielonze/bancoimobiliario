from random import randint

class Player:
    def __init__(self, type):
        self.type = type
        self.playing = True
        self.wallet = 300
        self.currentPosition = -1
        self.properties = []

    def payRent(self, property):
        if property.rent <= self.wallet:
            property.owner.wallet += property.rent
            self.wallet -= property.rent
        else:
            self.playing = False
            property.owner.wallet += self.wallet
            for p in self.properties:
                p.owner = None


    def buyOrPass(self, property):
        if self.type == "impulsive":
            self.impulsivePlayer(property)
        elif self.type == "demanding":
            self.demandingPlayer(property)
        elif self.type == "cautious":
            self.cautiousPlayer(property)
        elif self.type == "random":
            self.impulsivePlayer(property)
        else:
            print("Unknown type", self.type)

    def impulsivePlayer(self, property):
        if (property.price < self.wallet):
            property.buy(self)
            self.properties.append(property)

    def demandingPlayer(self, property):
        if (property.price < self.wallet and property.rent > 50):
            property.buy(self)
            self.properties.append(property)
    
    def cautiousPlayer(self, property):
        if (self.wallet - property.price > 80):
            property.buy(self)
            self.properties.append(property)

    def randomPlayer(self, property):
        if (property.price < self.wallet and randint(0, 1) == 1):
            property.buy(self)
            self.properties.append(property)

    def rollTheDice(self):
        return randint(1, 6)

    def movePlayer(self):
        self.currentPosition += self.rollTheDice()
        if self.currentPosition >= 20:
            self.wallet += 100
        self.currentPosition %= 20


