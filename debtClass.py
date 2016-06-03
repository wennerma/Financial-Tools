class Debts:
    def __init__(self, name, principal, apr, term):
        self.name = name
        self.principal = principal
        self.apr = apr                #given in decimal form
        self.mApr = apr/12
        self.term = term              #specified in years
        self.totalNumPayments = term*12
        self.totalSpent = 0
        self.mPayment = 0
        self.interest = 0
        self.type = 'Debt'

    def amoritizationTable(self):
        print("Table")

    def totalSpend(self):
        if (self.totalSpent == 0):
            self.monthlyPayment()
            self.totalSpent = self.totalNumPayments*round(self.mPayment,2)
            self.interest = self.totalSpent - self.interest

            

    def monthlyPayment(self):
        if(self.mPayment == 0):
            #P*(J/(1-(1+J)^-N))
            calc1 = 1 - pow(1+self.mApr,self.totalNumPayments * (-1))
            self.mPayment = self.principal * (self.mApr/calc1)
            

        
        
        
    
