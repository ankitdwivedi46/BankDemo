from Utility.DBConnections import DBConnections
from AccountOpenModuel.OpenAccount import OpenAccount
import pandas as pd
from datetime import datetime

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

        SQL_QUERY = "INSERT INTO CUSTOMER_ACCOUNT ([CUSTOMER_ACC_NO],[CUSTOMER_BALANCE]) VALUES('{}','{}')".format(
         str(openAcc.get_cust_acc_no()),"0")

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()

        SQL_QUERY = "CREATE TABLE CUSTOMER_{} (CUSTOMER_ACC_NO NVARCHAR(36) PRIMARY KEY,CHANGE_AMOUNT NVARCHAR(50) NOT NULL,CREDIT_FLAG CHAR(1) NOT NULL,DEBIT_FLAG CHAR(1) NOT NULL, MODIFIED_TIME NVARCHAR(50) NOT NULL, ACC_BALANCE NVARCHAR(50) NOT NULL )".format(str(openAcc.get_cust_acc_no()))

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()

        SQL_QUERY = "INSERT INTO CUSTOMER_{} ([CUSTOMER_ACC_NO],[CHANGE_AMOUNT],[CREDIT_FLAG],[DEBIT_FLAG],[MODIFIED_TIME],[ACC_BALANCE]) VALUES('{}','{}','{}','{}','{}','{}')".format(
            str(openAcc.get_cust_acc_no()),str(openAcc.get_cust_acc_no()),"0","T","F",str(datetime.utcnow()),"0")

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()

        conn.close()

    
    

        



        

