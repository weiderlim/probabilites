# a script that simulates a game of roulette being played. Only encompasses the 36 numbers for now. 
import random
import time 
from game import Game

# betting strategy and it's outcome                    
bets = [
    {"bet_amt" : 5, "bet_nums" : [1, 2, 3, 4]}, 
    {"bet_amt" : 10, "bet_nums" : [10, 11]}
]

num_tries = 10000
cash = 1000

for x in range(1, num_tries) : 
    print ("GAME NUMBER " + str(x))
    game = Game(bets)
    
    cash += game.payout()
    cash -= game.bet_amt()
    
    print("Current Cash :" + str(cash))
    print("\n")
    # time.sleep(0.5) 

