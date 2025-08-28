import sys
attemps = 1

def menu():
    print("""
        ---------------------------ATM---------------------------
[1] - View Balance
[2] - Deposit Money
[3] - Withdraw Money
[4] - Change PIN
[5] - Mini Statement (last 5 transactions)
[6] - Exit

        """)
    a = int(input("Enter choice : "))
    choice(a)
def arrayclean():
    for i in range(len(transaction)-1):
        transaction[i] = transaction[i+1]
    del transaction[4]

def choice(a):
    global account_bal
    global transaction
    if a == 1:
        print("your Account Balance is ",account_bal)
        menu()
        
    elif a == 2:
        amount = float(input("Enter amount to deposit: "))
        account_bal = account_bal + amount
        if len(transaction) >= 5:
                arrayclean()
                transaction.append(['Deposit |',amount,'| Balance:',account_bal])
        else:
                transaction.append(['Deposit |',amount,'| Balance:',account_bal])
        print("your Account Balance is ",account_bal)
        menu()
        
    elif a == 3:
        amount = float(input("Enter amount to withdrawal: "))
        if account_bal >= amount: 
            account_bal = account_bal - amount
            if len(transaction) >= 5:
                arrayclean()
                transaction.append(['Withdrawal |',amount,'| Balance:',account_bal])
            else:
                transaction.append(['Withdrawal |',amount,'| Balance:',account_bal])
            print("your Account Balance is ",account_bal)
        else :
            print("Insufficient Balance")
            print("your Account Balance is ",account_bal)
        menu()

    elif a == 4:
        new_pw = int(input("Enter new password : "))
        account_no = new_pw
        print("Your new password is : ",account_no)

    elif a == 5:
        if  len(transaction)==0:
            print("No transactions yet")
        for i in range (len(transaction)):
            for j in range (1):
                print(transaction[i][j],transaction[i][j+1],transaction[i][j+2],transaction[i][j+3])
        menu()

    elif a == 6:
        sys.exit(0)
        
        
        
        
while attemps <=3:
    
    account_bal = 5000.00
    account_no = 123456
    account_password = 1234
    
    transaction = []
    

    acc_No = int(input("Enter Account Number : "))
    acc_pass = int(input("Enter Password : "))
    
    if acc_No == account_no and acc_pass == account_password :
        attemps = 4
        menu()
        
        

    elif attemps == 3:
        print("Your account has been locked")
        break
    else:
         print("Invalid Username or password")
         attemps = attemps + 1

    




        
