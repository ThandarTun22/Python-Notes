import random
import string
# print('Welcome to password picker!')

adjectives = ['sleepy', 'slow', 'smelly',
            'wet', 'fat', 'red',
            'orange', 'yellow', 'green',
            'blue', 'purple', 'fluffy',
            'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball',
        'toaster', 'goat', 'dragon',
        'hammer', 'duck', 'panda']

special_chars = ['!','@','#','$','%','&','*','^','(',')']

passwords = []

while True:

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(special_chars)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    # response_add = input('Do you want to add your password into database? Type y or n')
    # if response_add.lower() == 'y':
    passwords.append(password)

    response = input("Would you like another password? Type y or n : ")
    if response.lower() == 'n':
        break

passwords_backup = passwords.copy()
print(passwords)
# print(passwords.count())

print(f'your password in database are : ')
for psw in passwords:
   print(psw)

resp = input("What do you want , Add , Remove , Delete ?")
if resp == 'Add':
    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)
    passwords.append(password)
elif resp == 'Remove':
    rem = input('Please Enter you want to delete : ')
    delete = passwords.index(rem)
    passwords.pop(delete)
elif resp == 'Delete':
    passwords.clear()
print("Passwords in databases :")
print(passwords)
