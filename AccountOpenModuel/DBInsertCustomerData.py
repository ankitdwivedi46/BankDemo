from Utility.DBConnections import DBConnections
from AccountOpenModuel.OpenAccount import OpenAccount
import pandas as pd

class DBInsertCustomerData:

    def insertDBCustomerData(self,obj):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        openAcc = obj

        SQL_QUERY = "INSERT INTO CUSTOMER_DATA ([CUSTOMER_NAME],[CUSTOMER_MOBILE],[CUSTOMER_EMAIL],[CUSTOMER_DOB],[CUSTOMER_AADHAR],[CUSTOMER_PAN],[CUSTOMER_ACC_NO],[CUSTOMER_IFSC],[CUSTOMER_ADDRESS]) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(str(openAcc.get_cust_name()),
        str(openAcc.get_cust_mobile()),str(openAcc.get_cust_email()),str(openAcc.get_cust_dob()),str(openAcc.get_cust_aadhar()),str(openAcc.get_cust_pan()),
        str(openAcc.get_cust_acc_no()),"12345",str(openAcc.get_cust_address()))

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()
        conn.close()

    
    

        



        

