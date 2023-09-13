# # first Que
# checkLeapYear = int(input("Enter a Leap year date"))

# if checkLeapYear%400 == 0 and checkLeapYear %100 == 0:
#     print("leap Year")
# elif checkLeapYear%4 == 0 and checkLeapYear%100 != 0:
#     print("Leap Year")
# else:
#     print("Not a leap year")

# # second que

checkEmail = input("Enter a email ? ")

if checkEmail.endswith(".com") and "@" in checkEmail:
    print("Correct email")
else:
    print("Not correct")
