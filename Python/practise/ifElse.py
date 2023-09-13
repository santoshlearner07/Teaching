WantToEat = True
WantToDrink = True

# if WantToEat and WantToDrink:
#     print("Lets Have a Pizza")
# else:
#     print("I am Good")

# if WantToEat or WantToDrink:
#     print("Lets Have a Pizza")
# else:
#     print("I am Good")

# if WantToEat:
#     print("Lets Have a Pizza")
# elif WantToDrink:
#     print("Lets have a drink")
# else:
#     print("I am good")

# name1 = input("Enter the Name ? ")
# per1Wallet = input("How much money you have ? ")

# name2 = input("Enter the Name ? ")
# per2Wallet = input("How much money you have ? ")

# name3 = input("Enter the Name ? ")
# per3Wallet = input("How much money you have ? ")

# if int(per1Wallet) > int(per2Wallet) and int(per1Wallet) > int(per3Wallet):
#     print(name1 + "Is the Richest")
# elif int(per2Wallet) > int(per1Wallet) and int(per2Wallet) > int(per3Wallet):
#     print(name2 + "Is the Richest")
# elif int(per3Wallet) > int(per1Wallet) and int(per3Wallet) > int(per1Wallet):
#     print(name3 + "Is the Richest")


def question():
    rules = input("You need to ans Every Question by yes or no, Do You Understand  ? ")
    if rules != "yes":
        return print("Try Again")
    else:
        print("next Question")
    Question1= input("Are you Hungry ? ")
    if Question1 == "no":
        return print("Lets go for a walk")
    else:
        print("next Question")
    Question2= input("Do you want to eat ? ")
    if Question2 == "no":
        return print("Fine GO Home")
    else:
        print("Next Question")
    Question3= input("What to you want to eat ? ")
    if Question3 == "no":
        print("Die")
    else:
        print("Lets eat a pizza")

question()