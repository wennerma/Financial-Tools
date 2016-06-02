from investmentClass import *
from debtClass import *
from inputController import *

lineInfo = inputer()
while(True):
    selection = int(input("Enter 1 for debt calculator, 2 for investments, 3 for analysis: "))
    inputList = []
    inputList = lineInfo.inputInfo(selection)
    
