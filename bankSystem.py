import random
import sys

database = {}

class Atm():
    def __init__(self, account_number):
        # self.name = name
        self.account_number = account_number
        # self.balance = balance

    def account_info(self):
        print("\n - - - - - - - - - - Account Information - - - - - - - - - - - ")
        # print(f" Account Holder : {self.name.upper()}")
        print(f" Name : {database[self.account_number]['username']}")
        print(f" Account Number : {self.account_number}")
        print(f" Available balance : {database[self.account_number]['amount']} \n")

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        database[self.account_number]['amount'] += self.deposit_amount
        print('Balance : ', database[self.account_number]['amount'])

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        database[self.account_number]['amount'] -= self.withdraw_amount
        print(' Balance : ', database[self.account_number]['amount'])

    def cash_transfer(self, transfer_account, transfer_amount):
        self.transfer_amount = transfer_amount
        self.transfer_account = transfer_account
        database[self.account_number]['amount'] -= self.transfer_amount
        database[self.transfer_account]['amount'] += self.transfer_amount
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

    database[account_no] = {}
    database[account_no]['username'] = username
    database[account_no]['password'] = password
    database[account_no]['amount'] = 0
    print('Account registration successful!')
    print('Account Number :', account_no)
    print('---------------------------------------')

    return username , account_no 

def signIn():

    print("- - - - Welcome to python ATM Machine - - - - \n")
    print("    Please sign in your account first... \n ")

    try:
        user_account  = int(input('Account No : '))
        print('- - - - - - - - - - - - - - - - - - - - - - - -')
    except ValueError:
        print ( " User account must be number !")
        signIn()
    # ValueError: invalid literal for int() with base 10: 'klo'
    
    if user_account not in database:
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
        while database[user_account]['password'] != password:
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
        user_account   = signIn()   
            
        atm = Atm( user_account)

        user_option = atm.transaction()

        while user_option != '5':

            if user_option == '1':
                atm.account_info()

            elif user_option == '2':               
                try:                  
                    deposit_amount = int(input('Enter amount to deposit : '))
                    atm.deposit(deposit_amount)  
                except ValueError:
                    print("Deposit amount must be number !")
                    deposit_amount = int(input('Enter amount to deposit : '))

            elif user_option == '3':
                withdraw_amount = int(input('Enter amount to withdraw : '))
                while withdraw_amount > database[user_account]['amount'] :
                    print('Your balance is  insufficient! ')
                    print('Balance : ', database[user_account]['amount'])
                    withdraw_amount = int(input('Enter amount to withdraw : '))
                atm.withdraw(withdraw_amount)

            elif user_option == '4':              
                transfer_account = int(input('Enter account you want to transfer ! : '))
                # while transfer_account not in database:
                #     print('Your transfer account is not registered! ')
                #     print('Please enter registered account! and Try again !')
                #     transfer_account = input('Enter account you want to transfer ! : ')

                transfer_amount = int(input('Enter amount to transfer : '))
                while transfer_amount > database[user_account]['amount'] :
                    print('YOur balance is not insufficient! ')
                    print('Balance : ', database[user_account]['amount'])
                    transfer_amount = int(input('Enter amount to transfer : '))
                atm.cash_transfer(transfer_account, transfer_amount)

                # print(database)

            user_option = atm.transaction()         

    else:
        print('Invalid option')
        sys.exit()

    print('################################')
    status = home()
