from Utility.CommonFunctions import CommonFunctions
from MoneyWithdrawlModuel.DBUpdateAfterWithdrawl import DBUpdateAfterWithdrawl

class MoneyWithdraw:

    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__pin = ""
        self.__acc_no = ""
        self.__amount = ""

    def fetchDetailsFromUser(self):

        cfObj = CommonFunctions()

        self.username = input("Enter User Name to Login: ")
        choice = input("Want to login using PIN or Password: ")
        if(choice.upper() == "PIN"):
            self.pin = input("Enter the PIN").upper()
            self.acc_no = cfObj.validateCustomerPIN(self.username,self.pin)
        elif(choice.upper()=="PASSWORD"):
            self.password = input("Enter the Password: ")
            self.acc_no = cfObj.validateCustomerPassword(self.username,self.password)

        print("==============LOGIN SUCCESSFUL===============")

        self.amount = input("Enter Amount to be Withdrawn: ")
        cfObj.validateCustomerBalance(self.acc_no,self.amount)

        print("Enter the PIN again: ")
        cfObj.validateCustomerPIN(self.username, self.pin)

        print("=============PLEASE COLLECT YOUR AMOUNT==============")

    def updateDBAfterMoneyWithdraw(self):

        obj = DBUpdateAfterWithdrawl()
        obj.updateDBAfterWithdrawl(self.amount,self.acc_no)







