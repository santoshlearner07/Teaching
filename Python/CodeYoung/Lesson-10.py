# for i in range(1, 10):
#     for j in range(1, 11):
#         print(i,j,"i * j\n")
# print("")

# for i in range(1,7):
#     for j in range(1,7):
#         for k in range(1,7):
#             print(i*j*k,"Total Value first")


# primeNumber = int(input("Enter a Number"))

# if primeNumber == (1 or 2 or 3):
#     print(primeNumber, "is a primeNumber")
# elif primeNumber > 4:
#     for i in range(4, primeNumber):
#         if (primeNumber % i) == 0:
#             # print(primeNumber, "Not a Prime Number")
#             break
#         else:
#             print(primeNumber, "Is a Prime Number")
# else:
#     print(primeNumber, "Not a prime number")

number = int(input("Enter a Number"))
n1,n2=0,1
# count = 0
for i in range(0,number + 1):
    print(n1)
    num = n1+n2
    n1=n2
    n2=num    
