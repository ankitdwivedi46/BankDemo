import pandas as pd

from Utility.DBConnections import DBConnections

class CommonFunctions:

    def validateCustomer(self,acc_no):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_DATA WHERE CUSTOMER_ACC_NO='{}'".format(acc_no),conn))>0

        conn.close()

    def validateCustomerPIN(self,username,pin):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert (pd.read_sql_query("SELECT CUSTOMER_PIN FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_USERNAME='{}'".format(username), conn)['CUSTOMER_PIN'][0]) == pin

        conn.close()

    def validateCustomerPassword(self,username,password):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        from cryptography.fernet import Fernet

        key = pd.read_sql_query("SELECT DECRYPT_KEY FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_USERNAME='{}'".format(username), conn)['DECRYPT_KEY'][0].encode("utf-8")
        pass_word = pd.read_sql_query("SELECT CUSTOMER_PASSWORD FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_USERNAME='{}'".format(username), conn)['CUSTOMER_PASSWORD'][0].encode("utf-8")

        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.decrypt(bytes(pass_word))

        assert ciphered_text.decode("utf-8") == password

        conn.close()






