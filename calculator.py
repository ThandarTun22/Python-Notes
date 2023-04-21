
# calculator
# violet

# add
def add(n1, n2):
    return n1 + n2

# subtract
def sub(n1, n2):
    return n1 - n2

# multiply
def mult(n1, n2):
    return n1 * n2

# divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}
def calculator():

    try:
        num1 = float(input("What is the first number? : "))
        writeFile = open("sample.txt","a")
        writeFile.write(f"first number is{num1}" + "\t")
        writeFile.close()

        for symbol in operations:
            print(symbol)

        should_continue = True
        while should_continue:

            operation_symbol = input("Pick an operation : ")
            num2 = float(input("What is the next number? : "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")
            if input(f"Type 'y' to continue calculating whth {answer}, or type 'n' to start a new calcultion: ") == "y":
                num1 = answer
                writeFile = open("sample.txt","a")
                writeFile.write(f"next number is{num2}" + "\t")
                writeFile.close()
            else:
                should_continue = False
                
        
        writeFile = open("sample.txt","a")
        writeFile.write("\n")
        writeFile.close()
    except ValueError as e:
        print("could not convert string to float , Please enter a number")
    except ZeroDivisionError as e:
        print("cannot divided by zero")
    except KeyError as e:
        print("Please enter an operan '+ - * / ' only ")
    except TypeError as e:
        print(" unsupported operand type(s) for +: 'float' and 'str', please enter a number")
    except Exception as e:
        print("Invalid")
    
calculator()

writeFile = open("sample.txt","r")
datafile = writeFile.read()
print(datafile)
writeFile.close()
