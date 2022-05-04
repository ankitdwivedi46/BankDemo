from Utility.CommonFunctions import CommonFunctions

class MoneyWithdraw:

    username = ""
    password = ""
    pin = ""

    def fetchDetailsFromUser(self):

        cfObj = CommonFunctions()

        self.username = input("Enter User Name to Login: ")
        choice = input("Want to login using PIN or Password: ")
        if(choice.upper() == "PIN"):
            self.pin = input("Enter the PIN").upper()
            cfObj.validateCustomerPIN(self.username,self.pin)
        elif(choice.upper()=="PASSWORD"):
            self.password = input("Enter the Password: ")
            cfObj.validateCustomerPassword(self.username,self.password)




