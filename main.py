from investmentClass import *
from debtClass import *
from inputController import *
from outPutController import *

lineInput = Inputer()
outPut = Outputter()
while(True):
    assetList = []   #holds multiple debts and investments
    assetList = lineInput.mainSelection()
    if(len(assetList) < 2):
        if(assetList[0].type == 'Invest'):
            assetList[0].compoundInterest()
            outPut.compoundInterestOut(assetList[0])
        else:
            debtSelection = lineInput.debtSelector()
            if(debtSelection == 4):
                assetList[0].monthlyPayment()
                outPut.monthlyPaymentOut(assetList[0])
            elif(debtSelection == 5):
                assetList[0].totalSpend()
                outPut.totalSpendOut(assetList[0])
            elif(debtSelection == 6):
                assetList[0].amoritizationTable()
                outPut.amortizationOut(assetList[0])              
                

          
            
                        
    
        
  
        
