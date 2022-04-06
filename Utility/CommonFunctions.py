import pandas as pd

from Utility.DBConnections import DBConnections

class CommonFunctions:

    def validateCustomer(self,acc_no):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_DATA WHERE CUSTOMER_ACC_NO='{}'".format(acc_no),conn))>0

        conn.close()

    def validateCustomerCred(self,acc_no):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        assert len(pd.read_sql_query("SELECT * FROM CUSTOMER_CREDENTIAL_DATABANK WHERE CUSTOMER_ACC_NO='{}'".format(acc_no), conn)) == 0

        conn.close()






