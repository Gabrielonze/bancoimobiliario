from .game import Game

class GameRun(object):
    def __init__(self):
        self.resultSum = {
            "runs": 0,
            "timeoutRuns": 0,
            "avgMoves": 0,
            "impulsive": 0,
            "demanding": 0,
            "cautious": 0,
            "random": 0,
        }

    def run(self):
        for x in range(300):
            game = Game()
            run = game.startGame()
            self.resultSum["runs"] += 1
            if run["moves"] == 1000:
                self.resultSum["timeoutRuns"] += 1
            self.resultSum[run["winner"]] += 1
            self.resultSum["avgMoves"] += run["moves"]

        
        self.resultSum["avgMoves"] /= self.resultSum["runs"]
        self.resultSum["impulsive"] /= self.resultSum["runs"]
        self.resultSum["demanding"] /= self.resultSum["runs"]
        self.resultSum["cautious"] /= self.resultSum["runs"]
        self.resultSum["random"] /= self.resultSum["runs"]
            
        return self.resultSum
