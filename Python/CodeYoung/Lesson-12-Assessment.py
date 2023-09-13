# Creating a calculator


while True:

    operation = input("select \n 1 for +\n 2 for - \n 3 for * \n 4 for / \n  0 to end Calculator \n  ")

    if operation == "0":
        print("Exiting")
        break

    firstNumber = int(input("Enter the first number."))
    secondNumber = int(input("Enter the second number."))
    if operation == "1" :
        print("Result:" , (firstNumber + secondNumber))
    elif operation == "2":
        print("Result:" , (firstNumber - secondNumber))
    elif operation == "3":
            print("Result:" , (firstNumber * secondNumber))
    elif operation == "4":
            print("Result:" , (firstNumber / secondNumber))
    else:
        print("Operation Not Correct")