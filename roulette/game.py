import random
import time 

class Game : 
    def __init__ (self, bets) :         
        # put this in the format of : [{bet_amt : 5, bet_nums : [1, 2, 3, 4]}, {bet_amt : 10, bet_nums : [10, 11]}
        self.bets = bets        

        self.nums = list(range (0, 37)) 
        self.rule_check ()
        # payout ratio default is 36, used to calculate the payout to player. 37 is not even enough to break even because they have -1 in payout formula
        self.payout_ratio = 36
        # self.payout ()


    def rule_check (self) : 
        for bet in self.bets : 
            if len (bet["bet_nums"]) not in [1, 2, 4] : 
                print ("Bets can only be placed within 1, 2, or 4 numbers")
                return None


    def bet_amt (self) : 
        curr_amt = 0
        
        for bet in self.bets : 
            curr_amt += bet["bet_amt"] 

        print ("Bet Total : " + str(curr_amt))
        
        return curr_amt 
        

    def roll_roulette (self) : 
        result = random.choice (self.nums)
        print ("Roll Result : " + str(result))
        
        return result 


    def payout (self) : 
        roll_result = self.roll_roulette() 

        curr_payout = 0

        for bet in self.bets : 
            for num in bet["bet_nums"] : 
                if num == roll_result : 
                    num_count = len (bet["bet_nums"])
                    # example : (36 / 2) - 1 = 17 for two numbers
                    curr_payout += bet["bet_amt"] * ((self.payout_ratio / num_count) - 1)

        print ("Payout : " + str(curr_payout))

        return curr_payout

