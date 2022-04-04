from AccountOpenModuel.AccNoGenerator import AccNoGenerator
from AccountOpenModuel.OpenAccount import OpenAccount
from AccountOpenModuel.DBInsertCustomerData import DBInsertCustomerData
from AccountOpenModuel.VerifyUserDetails import VerifyUserDetails

class RunOpenAccount:

    def fetchUserDetail(self):

        openAcc = OpenAccount()
        genAccNo = AccNoGenerator()
        verifyUser = VerifyUserDetails()

        cust_name = str(input("Please enter your full name: ")).upper()
        verifyUser.verifyCustName(cust_name.replace(" ",""))
        openAcc.set_cust_name(cust_name)
        cust_mobile = str(input("Please enter your mobile no: "))
        verifyUser.verifyCustMobile(cust_mobile)
        openAcc.set_cust_mobile(cust_mobile)
        cust_email = str(input("Please enter your email: ")).upper()
        verifyUser.verifyCustEmail(cust_email)
        openAcc.set_cust_email(cust_email)
        cust_dob = str(input("Please enter your date of birth(dd-mm-yyyy): "))
        verifyUser.verifyCustDob(cust_dob)
        openAcc.set_cust_dob(cust_dob)
        cust_aadhar = str(input("Please enter your aadhar: "))
        verifyUser.verifyCustAadhar(cust_aadhar)
        openAcc.set_cust_aadhar(cust_aadhar)
        cust_pan = str(input("Please enter your pan: ")).upper()
        verifyUser.verifyCustPan(cust_pan)
        openAcc.set_cust_pan(cust_pan)
        cust_address = str(input("Please enter your address: ")).upper()
        openAcc.set_cust_address(cust_address)
        cust_acc_no = genAccNo.accNoGenerator(openAcc).upper()
        openAcc.set_cust_acc_no(cust_acc_no)

        return openAcc

    def insertUserDetailDB(self,obj):

        dbins = DBInsertCustomerData()

        dbins.insertDBCustomerData(obj)

