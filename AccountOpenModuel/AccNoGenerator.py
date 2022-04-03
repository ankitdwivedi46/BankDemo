from AccountOpenModuel.OpenAccount import OpenAccount


class AccNoGenerator:

    def __init__(self):
        self.__acc_no = ""


    def accNoGenerator(self,obj):

        self.__acc_no = str(obj.get_cust_mobile())[0:3]+str(obj.get_cust_aadhar())[0:3]+str(obj.get_cust_pan())[0:3]

        return self.__acc_no