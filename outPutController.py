from debtClass import *
from investmentClass import *

class Outputter:
    def compoundInterestOut(self, investment):
        print("Investment: %s" % investment.name)
        print("Initial balance: %.02f" % investment.startingBalance)
        print("Annual Deposit: %.02f" % investment.annualDeposit) 
        print("Project growth rate: %.02f" % investment.rate)
        print("Value after %i years is %.02f \n" % (investment.term,investment.projectedValue))

    def monthlyPaymentOut(self, debt):
        print("Debt: %s" % debt.name)
        print("Principal: %.02f" % debt.principal)
        print("Term: %i years" % debt.term)
        print("APR: %.03f" % debt.apr)
        print("Monthly payment: %.02f \n" % debt.mPayment)

    def totalSpendOut(self, debt):
        print("Principal: %.02f" % debt.principal)
        print("Interest: %.02f" % debt.interest)
        print("Total: %.02f" % debt.totalSpent)

        
