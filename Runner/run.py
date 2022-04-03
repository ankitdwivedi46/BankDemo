from AccountOpenModuel.RunOpenAccount import RunOpenAccount


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

var = input(" Please enter what you want to do : ")

if( var == "1" ):

    openAcc = RunOpenAccount()
    obj = openAcc.fetchUserDetail()
    openAcc.insertUserDetailDB(obj)


    


