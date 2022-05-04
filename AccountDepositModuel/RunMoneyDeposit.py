from Utility.CommonFunctions import CommonFunctions
from AccountDepositModuel.UpdateDBWithMoneyDepositData import UpdateDBMoneyDeposit

class MoneyDeposit:

    cust_acc_no = ""
    amount = ""

    def fetchMoneyDetailsFromUser(self):

        cfObj = CommonFunctions()

        cust_acc_no = input("Enter the account no in which you want to deposit the money: ").upper()
        cfObj.validateCustomer(cust_acc_no)

        amount = input("Enter the amount you want to deposit: ")



    def updateDepositMoneyInDB(self):

        dBUpd = UpdateDBMoneyDeposit()
        dBUpd.updateDatabaseWithMoneyDepositData(self.cust_acc_no,self.amount)



