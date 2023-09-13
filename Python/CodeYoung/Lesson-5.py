# word  = 'SuperMan'
# print(word[1])
# print(word[-5])
# print(word[2:7])
# print(word[2:])
# print(word[:7])
# word2 = "Hello"
# print(word + word2)

# sentence = f'{word2} {word} '
# print(sentence)

# nameForPet = input("Enter the puppy Name")
# # print(f'{nameForPet} is the puppy name')
# # print(nameForPet[ : : -1])
# if nameForPet == nameForPet[ : : -1]:
#     print(f'{nameForPet} is a Palindrome')
# else:
#     print(f'{nameForPet} not a palindrome')


# # second que
# values = [1,2,3,4,5,6,7,8,9]
# response = values[ : :2] + values[1 :  : 2]
# print(response)

# sentence = input("Enter your sentence ? ")
# evenWords = sentence[0: :2]
# oddWords =  sentence[1 : :2]
# print(evenWords + oddWords)

# # check Valid Phone Number
number = input("Enter the Number")
# print(len(number))
# print(number.isnumeric())
# print(number[0])

if len(number) == 10 and number.isnumeric() and (number[0] == 7 or 8 or 9 ):
    print("Valid Number")
else:
    print("Not a valid number check again") 