

import random
import sys


database = {}
hotel_info = {}

class Hotel():

    def __init__(self, booking_account):
        self.booking_account = booking_account

    def hotel_info():
        print("Hotel Information")


def home():
    print("--------------Welcome to HOtel----------------\n")
    return input(" 1. Sign in \t\t\t 2. Sign up ")

def signUp():
    print("-------------Welcome to Hotel ------------------\n")
    print("Please sigh up your account first \n")

    username = input("Name : ")
    age = input("Age : ")
    nrc = input("NRC : ")
    password = input("Password : ")
    confirm_password = input("Confirm Password : ")

    while password != confirm_password:
        print("Your password does not match ! ")
        password = ("Password : ")
        confirm_password = input("Confirm Password : ")

    book_account = random.randrange(1000000, 10000000)

    database[book_account] = {}

    database[book_account]['username'] = username
    database[book_account]['age'] = age
    database[book_account]['nrc'] = nrc
    database[book_account]['password'] = password

    print("Account Registration Successful!")
    print('Your Book Account Number : ', book_account)
    print("----------------------------------")


def signIn():

    print("Welcome to Hotel \n")
    print("Please sign in your account first \n")

    try:
        booking_account = int(input("Booking Account number : "))
        print("-----------------------------------------")

    except ValueError:
        print("User account must be number !")
        signIn()

    if booking_account not in database:
        print("Your booking account is not registered !")
        print("Please sign up and login again ! ")
        print("---------------------------------")

        user_option = home()

        if user_option == '2':
            signUp()

        elif user_option == '1':
            signIn
        
        else:
            sys.exit()
        
        return booking_account
    else:
        password = input('Password : ')
        while database[booking_account]['password'] != password:
            print('Wrong Password !')
            password = input("Password : ")
        print("Sign in successful!")
        return booking_account

status = home()

while True:

    if status == '2':
        signUp()

    elif status == '1':
       booking_account =  signIn()

       hotel = Hotel(booking_account)



    else:
        print('Invalid Option')
        sys.exit()

        


