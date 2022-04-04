from datetime import datetime
import re


class VerifyUserDetails:

    def verifyCustName(self,cust_name):

        assert len(cust_name) > 0
        assert len(cust_name) <= 50
        assert cust_name.isalpha() == True

    def verifyCustMobile(self,cust_mobile):

        assert len(cust_mobile) == 10
        assert cust_mobile.isdigit() == True

    def verifyCustEmail(self,cust_email):

        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
        assert bool(re.match(pat,cust_email)) == True

    def verifyCustDob(self,cust_dob):

        assert len(cust_dob) == 10
        assert bool(datetime.strptime(cust_dob, "%d-%m-%Y")) == True

    def verifyCustAadhar(self,cust_aadhar):

        assert len(cust_aadhar) == 12
        assert cust_aadhar.isdigit() == True

    def verifyCustPan(self, cust_pan):
        assert len(cust_pan) == 10
        assert cust_pan.isalnum() == True









