

class UserNamePassPIN:

    def __init__(self):
        self.__cust_username = ""
        self.__cust_password = ""
        self.__cust_pin = ""
        self.__cust_acc_no = ""
        self.__cust_first_login_flag = ""

    def get_cust_username(self):
        return self.__cust_username

    def set_cust_username(self,cust_username):
        self.__cust_username = cust_username

    def get_cust_password(self):
        return self.__cust_password

    def set_cust_password(self,cust_password):
        self.__cust_password = cust_password

    def get_cust_pin(self):
        return self.__cust_pin

    def set_cust_pin(self,cust_pin):
        self.__cust_pin = cust_pin

    def get_cust_acc_no(self):
        return self.__cust_acc_no

    def set_cust_acc_no(self,cust_acc_no):
        self.__cust_acc_no = cust_acc_no

