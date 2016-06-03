import math
class Investments:
    def __init__(self, name, startingBalance, annualDeposit, rate, term):
        self.name = name
        self.startingBalance = startingBalance
        self.rate = rate
        self.term = term
        self.annualDeposit = annualDeposit
        self.type = 'Invest'
        self.projectedValue = 0

    def compoundInterest(self):

        newBalance1 = self.startingBalance*pow((1 +  self.rate),self.term)
        newBalance2 = (pow((1 + self.rate),self.term)-1)/self.rate
        self.projectedValue = newBalance1 + self.annualDeposit*newBalance2

        
