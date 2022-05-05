from Utility.CommonFunctions import CommonFunctions
from AccountDepositModuel.UpdateDBWithMoneyDepositData import UpdateDBMoneyDeposit

class MoneyDeposit:

    def __init__(self):
        self.__cust_acc_no = ""
        self.__amount = ""

    def fetchMoneyDetailsFromUser(self):

        cfObj = CommonFunctions()

        self.cust_acc_no = input("Enter the account no in which you want to deposit the money: ").upper()
        cfObj.validateCustomer(self.cust_acc_no)

        self.amount = input("Enter the amount you want to deposit: ")


    def updateDepositMoneyInDB(self):

        dBUpd = UpdateDBMoneyDeposit()
        dBUpd.updateDatabaseWithMoneyDepositData(self.cust_acc_no,self.amount)



