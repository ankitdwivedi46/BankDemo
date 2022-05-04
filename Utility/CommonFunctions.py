import pandas as pd

from Utility.DBConnections import DBConnections

class CommonFunctions:

    def validateCustomer(self,acc_no):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_DATA WHERE CUSTOMER_ACC_NO='{}'".format(acc_no),conn))>0

        conn.close()

    def validateCustomerPIN(self,pin):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_PIN='{}'".format(pin), conn)) == 0

        conn.close()

    def validateCustomerPassword(self,password):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()

        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.decrypt(bytes(password, "utf-8"))

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_PASSWORD='{}'".format(password), conn)) == 0

        conn.close()






