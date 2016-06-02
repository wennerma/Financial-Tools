class Investments:
    def __init__(self, name, startingBalance, monthlyDeposit, rate, term):
        self.name = name
        self.startingBalance = startingBalance
        self.rate = rate
        self.term = term

    def compoundInterest():
        total = startingBalance*pow(1+rate,term)
        print(total)

