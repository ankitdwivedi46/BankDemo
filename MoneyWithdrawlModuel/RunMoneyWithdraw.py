from Utility.CommonFunctions import CommonFunctions

class MoneyWithdraw:

    username = ""
    password = ""
    pin = ""
    acc_no = ""
    amount = ""

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







