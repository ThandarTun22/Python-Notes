
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='root@123',
    database = 'testdb'
    )

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
# student1 = ("Rachel", 22)


# mycursor.execute(sqlFormula, student1)

# mycursor.execute("CREATE TABLE bank(ID int NOT NULL AUTO_INCREMENT, Name VARCHAR(255), AccountNumber VARCHAR(255), Amount INT, Password VARCHAR(255), PRIMARY KEY(ID))")
# mydb.commit()

# sqlInsert = "INSERT INTO bank (Name, AccountNumber, Amount, Password) VALUES(%s, %s, %s, %s)"
# userInfo = ("TT", 1234, 0, 123)
# mycursor.execute(sqlInsert, userInfo)
# mydb.commit()

# mycursor.execute("SELECT AccountNumber FROM bank")
# accountNumbe = mycursor.fetchall()
# print(accountNumbe)

# for account in accountNumbe:
#     print(account)

# password = 123
# mycursor.execute("SELECT Password FROM bank WHERE Password=password") 
# myresult = mycursor.fetchall()
# for result in myresult:
#     print(result)

# password = 123
# sql = "SELECT Password FROM bank WHERE Password= '%s' " % password
# mycursor.execute(sql)    
# passwordResult = mycursor.fetchall()
# print(passwordResult)
            
# while not passwordResult :
#     print('Wrong Password!')
#     input("enter password")
# print("Sign in successful!")

# deposit_amount  = 5000
# account_number = 1234
# sqldeposit = "UPDATE bank SET Amount = Amount + %s WHERE AccountNumber = %s " 
# values = (deposit_amount, account_number)
# mycursor.execute(sqldeposit, values)
# mydb.commit()

# withdraw_amount = 50000
# sqlBalance = "SELECT Amount FROM bank WHERE AccountNumber= 1234 " 
# mycursor.execute(sqlBalance) 
# balance = mycursor.fetchall()

# for amount in balance:
#     amount = int(amount[0])
#     while withdraw_amount > amount :
#         print('Your balance is  insufficient! ')
          
#         print(f" Available balance : {amount}")
#         withdraw_amount = int(input('Enter amount to withdraw : '))


mycursor.execute("SELECT AccountNumber FROM bank")
accountNumber = mycursor.fetchall()

for account in accountNumber:
    print(account)




# sql = "DROP TABLE students"
# mycursor.execute (sql)
# mydb.commit()