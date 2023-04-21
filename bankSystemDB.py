import random
import sys
import mysql.connector

db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='root@123',
    database = 'testdb'
    )
cursor = db.cursor()

# cursor.execute("CREATE TABLE bank(ID int NOT NULL AUTO_INCREMENT, Name VARCHAR(255), AccountNumber VARCHAR(255), Amount INT, Password VARCHAR(255), PRIMARY KEY(ID))")

# database = {}

class Atm():
    def __init__(self, account_number):       
        self.account_number = account_number
     

    def account_info(self, user_account):
        self.user_account = user_account
        print("\n - - - - - - - - - - Account Information - - - - - - - - - - - ")
        # print(f" Account Holder : {self.name.upper()}")
        # print(f" Name : {database[self.account_number]['username']}")
        # print(f" Account Number : {self.account_number}")
        # print(f" Available balance : {database[self.account_number]['amount']} \n")

        sqlUserName = "SELECT Name FROM bank WHERE AccountNumber= '%s' " % self.user_account
        cursor.execute(sqlUserName)
        userName = cursor.fetchall()
        for Uname in userName:
            nameStr = ''
            print(f" Name : {nameStr.join(Uname)}")

        sqlAccountNumber = "SELECT AccountNumber FROM bank WHERE AccountNumber= '%s' " % self.user_account
        cursor.execute(sqlAccountNumber)
        accountNumber = cursor.fetchall()
        for accountno in accountNumber:
            accountnumberstr = ''
            print(f" Account Number : {accountnumberstr.join(accountno)}")

        sqlBalance = "SELECT Amount FROM bank WHERE AccountNumber= '%s' " % self.user_account
        cursor.execute(sqlBalance) 
        balance = cursor.fetchall()
        for bamount in balance:
            bamount = int(bamount[0])   
            print(f" Available balance : {bamount}")

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        # database[self.account_number]['amount'] += self.deposit_amount
        # print('Balance : ', database[self.account_number]['amount'])
       
        sqldeposit = "UPDATE bank SET Amount = Amount + %s WHERE AccountNumber = %s " 
        valuesdeposit = (self.deposit_amount, self.account_number)
        cursor.execute(sqldeposit, valuesdeposit)
        db.commit()

        sqldBalance = "SELECT Amount FROM bank WHERE AccountNumber= '%s' " % self.account_number
        cursor.execute(sqldBalance) 
        dbalance = cursor.fetchall()
        for damount in dbalance:
            damount = int(damount[0])   
            print(f" Available balance : {damount}")

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        # database[self.account_number]['amount'] -= self.withdraw_amount
        # print(' Balance : ', database[self.account_number]['amount'])
        sqlwBalance = "SELECT Amount FROM bank WHERE AccountNumber= '%s' " % self.account_number
        cursor.execute(sqlwBalance) 
        wbalance = cursor.fetchall()

        for wamount in wbalance:
            wamount = int(wamount[0])
        while self.withdraw_amount > wamount :
            print('Your balance is  insufficient! ') 
            print(f" Available balance : {wamount}")
            self.withdraw_amount = int(input('Enter amount to withdraw : '))

        sqlwithdraw = "UPDATE bank SET Amount = Amount - %s WHERE AccountNumber = %s " 
        valueswithdraw = (self.withdraw_amount, self.account_number)
        cursor.execute(sqlwithdraw, valueswithdraw)
        db.commit()


    def cash_transfer(self, transfer_account, transfer_amount):
        self.transfer_amount = transfer_amount
        self.transfer_account = transfer_account
        # database[self.account_number]['amount'] -= self.transfer_amount
        # database[self.transfer_account]['amount'] += self.transfer_amount
        sqltBalance = "SELECT Amount FROM bank WHERE AccountNumber= '%s' " % self.account_number
        cursor.execute(sqltBalance) 
        balance = cursor.fetchall()

        for tamount in balance:
            tamount = int(tamount[0])
        while self.transfer_amount > tamount :
            print('YOur balance is not insufficient! ')
            print('Balance : ', tamount)
            self.transfer_amount = int(input('Enter amount to transfer : '))

        sqltransferfrom = "UPDATE bank SET Amount = Amount - %s WHERE AccountNumber = %s "
        valuetransferfrom = (self.transfer_amount, self.account_number)
        cursor.execute(sqltransferfrom, valuetransferfrom)
        db.commit()

        sqltransferto = "UPDATE bank SET Amount = Amount + %s WHERE AccountNumber = %s "
        valuetranferto = (self.transfer_amount, self.transfer_account)
        cursor.execute(sqltransferto, valuetranferto)
        db.commit()
        print("Transfer Successful! ")


    def transaction(self):
        print("- - - - Welcome to python ATM Machine - - - - \n")
        print("     Hello , what can I help you? ....")
        input_menu = input(" 1) Account Info \n 2) Deposits\n 3) Withdrawal \n 4) Cash Transfer \n 5) Sign Out")
        return input_menu

def signUp():
    print("- - - - Welcome to python ATM Machine - - - - \n")
    print("    Please sign up your account first... \n ")

    username = input('User Name : ')
    password = input('Password : ')
    confirm_password = input('Confirm Password : ')

    while password != confirm_password:
        print("Your password does not match ! ")
        password = input('Password : ')
        confirm_password = input('Confirm Password : ')

    account_no = random.randrange(100000000, 1000000000)
    # while account_no not in database:
    #     account_no = random.randrange(100000000, 1000000000)

    amount = 0
    sqlInsert = "INSERT INTO bank (Name, AccountNumber, Amount, Password) VALUES(%s, %s, %s, %s)"
    userInfo = (username, account_no, amount, password)
    cursor.execute(sqlInsert, userInfo)
    db.commit()

    # database[account_no] = {}
    # database[account_no]['username'] = username
    # database[account_no]['password'] = password
    # database[account_no]['amount'] = 0
    print('Account registration successful!')
    print('Account Number :', account_no)
    print('---------------------------------------')

    return username , account_no 

def signIn():

    print("- - - - Welcome to python ATM Machine - - - - \n")
    print("    Please sign in your account first... \n ")

    try:
        user_account  = input('Account No : ')
        print('- - - - - - - - - - - - - - - - - - - - - - - -')
    except ValueError:
        print ( " User account must be number !")
        signIn()
    # ValueError: invalid literal for int() with base 10: 'klo'
    
    sqlaccountNumber = "SELECT AccountNumber FROM bank WHERE AccountNumber= '%s' " % user_account
    cursor.execute(sqlaccountNumber)
    accountNumber = cursor.fetchall()

    for account in accountNumber:
        # print(account)
        account = int(account[0])

    if not account:
        print('Your account is not registered! ')
        print('Please sign up and login again !')
        print('- - - - - - - - - - - - - - - - - - - - - - - -')
        user_option = home()
        if user_option == '2':
            username, user_account = signUp()
            signIn()
        elif user_option == '1':
                signIn()
        else:
            sys.exit()
        return user_account
            
    else : 
        password = input('Password :')  
        sql = "SELECT Password FROM bank WHERE Password= '%s' " % password   
        cursor.execute(sql)    
        passwordResult = cursor.fetchall()
        # print(passwordResult)      
        # while database[user_account]['password'] != password:
        while not passwordResult:
            print('Wrong Password!')
            password = input('Password :')
        print("Sign in successful!")
        return user_account
             
def home():
    print("- - - - Welcome to python ATM Machine - - - - \n")
    return input("1) Sign In \t\t\t 2) Sign Up")

status = home()
while True:

    if status == '2':
        username , account_no  = signUp()      

    elif status == '1':
        userEnter_account   = signIn()   
            
        atm = Atm( userEnter_account)

        user_option = atm.transaction()

        while user_option != '5':

            if user_option == '1':
                atm.account_info(userEnter_account)

            elif user_option == '2':               
                try:                  
                    deposit_amount = int(input('Enter amount to deposit : '))
                    atm.deposit(deposit_amount)  
                except ValueError:
                    print("Deposit amount must be number !")
                    deposit_amount = int(input('Enter amount to deposit : '))

            elif user_option == '3':
                withdraw_amount = int(input('Enter amount to withdraw : '))
                # while withdraw_amount > database[user_account]['amount'] :
                #     print('Your balance is  insufficient! ')
                #     print('Balance : ', database[user_account]['amount'])
                #     withdraw_amount = int(input('Enter amount to withdraw : '))
                atm.withdraw(withdraw_amount)

            elif user_option == '4':              
                transfer_account = int(input('Enter account you want to transfer ! : '))
                # while transfer_account not in database:
                #     print('Your transfer account is not registered! ')
                #     print('Please enter registered account! and Try again !')
                #     transfer_account = input('Enter account you want to transfer ! : ')

                transfer_amount = int(input('Enter amount to transfer : '))
                # while transfer_amount > database[user_account]['amount'] :
                #     print('YOur balance is not insufficient! ')
                #     print('Balance : ', database[user_account]['amount'])
                #     transfer_amount = int(input('Enter amount to transfer : '))
                atm.cash_transfer(transfer_account, transfer_amount)

                # print(database)

            user_option = atm.transaction()         

    else:
        print('Invalid option')
        sys.exit()

    print('################################')
    status = home()
