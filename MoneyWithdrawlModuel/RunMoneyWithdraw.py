from Utility.CommonFunctions import CommonFunctions
from MoneyWithdrawlModuel.DBUpdateAfterWithdrawl import DBUpdateAfterWithdrawl
from Utility.CustomExceptions import InvalidPINException

class MoneyWithdraw:

    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__pin = ""
        self.__acc_no = ""
        self.__amount = ""

    def fetchDetailsFromUser(self):

        try:
            cfObj = CommonFunctions()

            self.username = input("Enter User Name to Login: ")
            choice = input("Want to login using PIN or Password: ")
            if(choice.upper() == "PIN"):
                self.pin = input("Enter the PIN").upper()
                if(cfObj.validateCustomerPIN(self.username,self.pin)==False):
                    raise InvalidPINException
                self.acc_no = cfObj.validateCustomerPIN(self.username,self.pin)
            elif(choice.upper()=="PASSWORD"):
                self.password = input("Enter the Password: ")
                self.acc_no = cfObj.validateCustomerPassword(self.username,self.password)

            print("==============LOGIN SUCCESSFUL===============")

            self.amount = input("Enter Amount to be Withdrawn: ")
            cfObj.validateCustomerBalance(self.acc_no,self.amount)

            self.pin = input("Enter the PIN again: ")
            cfObj.validateCustomerPIN(self.username, self.pin)

            print("=============PLEASE COLLECT YOUR AMOUNT==============")

        except InvalidPINException as err:
            print("Invalid PIN Entered")
            self.fetchDetailsFromUser()

    def updateDBAfterMoneyWithdraw(self):

        obj = DBUpdateAfterWithdrawl()
        obj.updateDBAfterWithdrawl(self.amount,self.acc_no)







