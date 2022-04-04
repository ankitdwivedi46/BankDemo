from AccountOpenModuel.RunOpenAccount import RunOpenAccount
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
    print(" 2. Money Deposit")
    print(" 3. Money Withdrawl")
    print(" 4. Account Update")
    print(" 5. Money Transfer")
    print(" 6. Account Close")
    print(" 7. Exit Bank App")

    print("================================================================================================")

    var = input(" Please enter what you want to do : ")

    if( var == "1" ):

        openAcc = RunOpenAccount()
        obj = openAcc.fetchUserDetail()
        openAcc.insertUserDetailDB(obj)
    elif( var == "7" ):

        break


    


