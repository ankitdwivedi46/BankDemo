from AccountOpenModuel.RunOpenAccount import RunOpenAccount
from UserNamePasswordPINModuel.RunGenerateCreds import RunGenerateCreds
from AccountDepositModuel.RunMoneyDeposit import MoneyDeposit
from MoneyWithdrawlModuel.RunMoneyWithdraw import MoneyWithdraw
import os




while(1):
    print("================================================================================================")
    print()
    print()
    print()

    print("                                     WELCOME TO ANKIT BANK                                      ")

    print()
    print()

    print(" 1. Account Opening")
    print(" 2. Generate UserName, Password and PIN")
    print(" 3. Money Deposit")
    print(" 4. Money Withdrawl")
    print(" 5. Account Update")
    print(" 6. Money Transfer")
    print(" 7. Account Close")
    print(" 8. Exit Bank App")

    print("================================================================================================")

    var = input(" Please enter what you want to do : ")

    if( var == "1" ):

        openAcc = RunOpenAccount()
        obj = openAcc.fetchUserDetail()
        openAcc.insertUserDetailDB(obj)
        print("Congratulations your account has opened. Account No : '{}'\nPlease generate UserName, Password and PIN for Net Banking login and Money Movement".format(str(obj.get_cust_acc_no())))

    elif( var == "2" ):

        genCred = RunGenerateCreds()
        obj1 = genCred.generateCreds()
        genCred.insertUserCredDB(obj1)

    elif (var == "3"):

        dep = MoneyDeposit()
        dep.fetchMoneyDetailsFromUser()
        dep.updateDepositMoneyInDB()

    elif (var == "4"):

        withDraw = MoneyWithdraw()
        withDraw.fetchDetailsFromUser()


    elif( var == "8" ):

        break


    


