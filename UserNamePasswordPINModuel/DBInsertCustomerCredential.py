from Utility.DBConnections import DBConnections
from UserNamePasswordPINModuel.UserNamePassPIN import UserNamePassPIN

class DBInsertCustomerCredential:

    def insertDBCustomerCred(self, obj):

        dbconn = DBConnections()
        conn = dbconn.connect_to_sql_server()

        credObj = obj

        from cryptography.fernet import Fernet
        key = Fernet.generate_key()

        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(bytes(credObj.get_cust_password(),"utf-8"))

        SQL_QUERY = "INSERT INTO CUSTOMER_CREDENTIAL_DATABANK([CUSTOMER_ACC_NO],[CUSTOMER_USERNAME],[CUSTOMER_PASSWORD],[CUSTOMER_PIN],[CUSTOMER_FIRST_LOGIN_FLAG]) VALUES('{}','{}','{}','{}','{}')".format(
            str(credObj.get_cust_acc_no()),str(credObj.get_cust_username()),ciphered_text.decode("utf-8"),str(credObj.get_cust_pin()),"T"
        )

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        conn.commit()


        conn.close()
