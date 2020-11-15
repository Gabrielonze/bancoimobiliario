from random import randint
from .models.Property import Property
from .models.Player import Player

class Game(object):
    def __init__(self):
        self.properties = []
        self.currentIndexPlayer = -1
        self.lastPlayer = None
        self.moves = 0
        self.playing = True 
        self.players = [
            Player("impulsive"),
            Player("demanding"),
            Player("cautious"), 
            Player("random")
        ]
        for x in range(20):
            self.properties.append(Property())

    def startGame(self):
        while self.playing and self.moves < 1000:
            self.currentIndexPlayer += 1
            self.currentIndexPlayer %= 4
            if self.players[self.currentIndexPlayer].playing:
                if self.lastPlayer == self.currentIndexPlayer:
                    self.playing = False
                else:
                    self.lastPlayer = self.currentIndexPlayer
                    self.doMove()

        # TODO: get richest player
        return {
            "moves": self.moves,
            "winner": self.players[self.currentIndexPlayer].type
        }

    def doMove(self):
        self.moves += 1
        self.players[self.currentIndexPlayer].movePlayer()
        currentProperty = self.properties[self.players[self.currentIndexPlayer].currentPosition]
        if currentProperty.owner != None:
            self.players[self.currentIndexPlayer].payRent(currentProperty)
        else:
            self.players[self.currentIndexPlayer].buyOrPass(currentProperty)
