
# # Que 1
# number =  int(input("Enter a number ?"))
# if number>0:
#     print("Postive")
# elif number<0   :
#     print("Negative")
# else :
#     print("Zero")

# # que 2

# if number%2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

print("Select Month by u \n January - 1 \n Feb -2 \n Mar-3\n Apr -4 \n May-5 \n June -6 \n July-7 \n Aug - 8 \n Sept - 9\n oct -10 \n Nov -11 \n Dec -12 \n")
monthNumber = int(input("Enter a Number ? "))
if monthNumber == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("31 Days") 
elif monthNumber  == 4 or 6 or 9 or 11 :
    print("30 Days")
else :
    print("28/29 Days")


