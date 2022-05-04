from Utility.DBConnections import DBConnections
from datetime import datetime
import pandas as pd

class UpdateDBMoneyDeposit:


    def updateDatabaseWithMoneyDepositData(self,acc_no,amount):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        SQL_QUERY = "SELECT CUSTOMER_BALANCE FROM CUSTOMER_ACCOUNT WHERE CUSTOMER_ACC_NO = '{}'".format(acc_no)
        print(SQL_QUERY)
        print(pd.read_sql_query(SQL_QUERY,conn))
        balance = pd.read_sql_query(SQL_QUERY,conn)['CUSTOMER_BALANCE'][0]

        new_bal = str((int(balance) + int(amount)))

        SQL_QUERY = "INSERT INTO CUSTOMER_{} ([CUSTOMER_ACC_NO],[CHANGE_AMOUNT],[CREDIT_FLAG],[DEBIT_FLAG],[MODIFIED_TIME],[ACC_BALANCE]) VALUES('{}','{}','{}','{}','{}','{}')".format(
            acc_no, acc_no, amount, "T", "F", str(datetime.utcnow()), new_bal)

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()

        SQL_QUERY = "UPDATE [CUSTOMER_ACCOUNT] SET CUSTOMER_BALANCE = '{}' WHERE CUSTOMER_ACC_NO = '{}'".format(new_bal,acc_no)

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()

        conn.close()