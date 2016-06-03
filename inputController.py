from debtClass import *
from investmentClass import *
class Inputer:
    def debtInfo(self):
        debtEntry = input("Enter debt name, principal, apr, term: ")
        debtVar = []
        debtVar = debtEntry.split(',')
        debt = Debts(debtVar[0], float(debtVar[1]), float(debtVar[2]), int(debtVar[3]))

        return debt

    def investInfo(self):
        investmentEntry = input("Enter you investment name, starting balance, annual deposit, rate, and term: ")
        investVar = []
        investVar = investmentEntry.split(',')
        invest = Investments(investVar[0], float(investVar[1]), float(investVar[2]), float(investVar[3]), int(investVar[4]))

        return invest

    def mainSelection(self):
        selection = int(input(" 1) Debt Calculator\n 2) Investments\n 3) Analysis:\n "))
        inputList = []
        if (selection == 1):
            debt = self.debtInfo()
            inputList.append(debt)
        elif (selection == 2):
            invest = self.investInfo()
            inputList.append(invest)
        elif (selection == 3):
            invest = self.investInfo()
            debt = self.debtInfo()
            inputList.append(invest)
            inputList.append(debt)

        return inputList

        
    def debtSelector(self):
        selection = int(input(" 4) Monthly Payment\n 5) Total Spent\n 6) Amoritazation Table:\n"))

        return selection
                     
