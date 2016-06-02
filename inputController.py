from debtClass import *
from investmentClass import *
class inputer:
    def debtInfo(self):
        debtEntry = input("Enter debt name, total amount, apr, term in months: ")
        debtVar = []
        debtVar = debtEntry.split(',')
        debt = Debts(debtVar[0], float(debtVar[1]), float(debtVar[2]), int(debtVar[3]))
        return debt

    def investInfo(self):
        investmentEntry = input("Enter you investment name, starting balance, annual deposit, rate, and term in months: ")
        investVar = []
        investVar = debtEntry.split(',')
        invest = Investments(investVar[0], float(investVar[1]), float(investVar[2]), int(investVar[3]))
        return invest

    def inputInfo(self,selection):
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
            
