# sentence = "Hello How do you do"

# for i in sentence:
#     print("First name",sentence[0])
#     if(i == "o"):
#         break
#     print(i)

# for i in sentence:
#     if (i=="o"):
#         continue
#     print(i)

# number = 24
# for i in range(1, 24):
#     if (number % i) == 0:
#         print(i)


for i in range(1, 25):
    for j in range(1, 61):
        for k in range(1, 61):
            print(i * j * k, "ijk")
            print(i,j,k)
            break