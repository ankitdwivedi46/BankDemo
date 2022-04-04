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
    print(" 2. Money Withdrawl")
    print(" 3. Account Update")
    print(" 4. Money Transfer")
    print(" 5. Account Close")

    print("================================================================================================")

    var = input(" Please enter what you want to do : ")

    if( var == "1" ):

        openAcc = RunOpenAccount()
        obj = openAcc.fetchUserDetail()
        openAcc.insertUserDetailDB(obj)


    


