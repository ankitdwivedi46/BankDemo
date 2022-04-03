from AccountOpenModuel.AccNoGenerator import AccNoGenerator
from AccountOpenModuel.OpenAccount import OpenAccount
from AccountOpenModuel.DBInsertCustomerData import DBInsertCustomerData

class RunOpenAccount:

    def fetchUserDetail(self):

        openAcc = OpenAccount()
        genAccNo = AccNoGenerator()

        cust_name = str(input("Please enter your full name: "))
        openAcc.set_cust_name(cust_name)
        cust_mobile = str(input("Please enter your mobile no: "))
        openAcc.set_cust_mobile(cust_mobile)
        cust_email = str(input("Please enter your email: "))
        openAcc.set_cust_email(cust_email)
        cust_dob = str(input("Please enter your date of birth(dd-mm-yyyy): "))
        openAcc.set_cust_dob(cust_dob)
        cust_aadhar = str(input("Please enter your aadhar: "))
        openAcc.set_cust_aadhar(cust_aadhar)
        cust_pan = str(input("Please enter your pan: "))
        openAcc.set_cust_pan(cust_pan)
        cust_address = str(input("Please enter your address: "))
        openAcc.set_cust_address(cust_address)
        cust_acc_no = genAccNo.accNoGenerator(openAcc)
        openAcc.set_cust_acc_no(cust_acc_no)

        return openAcc

    def insertUserDetailDB(self,obj):

        dbins = DBInsertCustomerData()

        dbins.insertDBCustomerData(obj)

