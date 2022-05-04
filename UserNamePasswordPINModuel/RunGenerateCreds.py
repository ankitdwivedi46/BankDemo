from Utility.CommonFunctions import CommonFunctions
from UserNamePasswordPINModuel.UserNamePassPIN import UserNamePassPIN
from UserNamePasswordPINModuel.DBInsertCustomerCredential import DBInsertCustomerCredential

class RunGenerateCreds:

    def generateCreds(self):

        cfObj = CommonFunctions()
        credObj = UserNamePassPIN()

        cust_acc = input("Enter Your Account No: ")
        cfObj.validateCustomer(cust_acc)
        cfObj.validateCustomer(cust_acc)
        credObj.set_cust_acc_no(cust_acc)

        cust_username = input("Enter User Name: ")
        credObj.set_cust_username(cust_username)

        cust_password = input("Enter User Password: ")
        credObj.set_cust_password(cust_password)

        cust_pin = input("Enter Customer PIN: ")
        credObj.set_cust_pin(cust_pin)

        return credObj

    def insertUserCredDB(self,obj):

        dbins = DBInsertCustomerCredential()
        dbins.insertDBCustomerCred(obj)


