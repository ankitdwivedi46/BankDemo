from AccountOpenModuel.OpenAccount import OpenAccount


class AccNoGenerator:

    def __init__(self):
        self.__acc_no = ""


    def accNoGenerator(self,obj):

        self.__acc_no = str(obj.get_cust_mobile())+str(obj.get_cust_aadhar())+str(obj.get_cust_pan())

        return self.__acc_no