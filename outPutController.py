from debtClass import *
from investmentClass import *
from datetime import datetime
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

    def amortizationOut(self, debt):
        count = 0
        flag = 0
        slidingPrincipal = debt.principal
        mPrincipal = 0
        mInterest = 0
        year = int(datetime.now().year)
        month = int(datetime.now().month)
        print("    Date    |  Principal |  Interest  |  Balance  ")
        for i in range(debt.term+1):
            if(flag == 1):
                break
            for j in range(12):
                mInterest = slidingPrincipal * debt.mApr
                mPrincipal = debt.mPayment-mInterest
                slidingPrincipal = slidingPrincipal - mPrincipal
                if(slidingPrincipal <= debt.mPayment):
                    flag = 1
                print("%4i" % month, end="-")
                print("%4i" % year, end= "      ")
                print("%.02f" % mPrincipal, end="      ")
                print("%.02f" % mInterest, end="       ")
                print("%.02f" % slidingPrincipal)
                count = count + 1
                if(count == debt.totalNumPayments):
                    flag = 1
                    break
                if(month == 12):
                    year = year + 1
                    month = 1
                    break
                month = month + 1

