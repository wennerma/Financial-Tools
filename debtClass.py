class Debts:
    def __init__(self, name, total, apr, term):
        self.name = name
        self.total = total
        self.apr = apr
        self.term = term

    def amoritizationTable(self):
        print("Debt: " + self.name)

    def totalSpend(self):
        total = self.total

    def monthlyPayment(self):
        monthly = self.total/self.term
        print(monthly)
        
    
