# footballTeam = []
# numOfPlayers = int(input("Number of players"))

# for i in range(numOfPlayers):
#     name = input("Player Name")
#     height = float(input("Enter the height"))

#     if height > 167:
#         footballTeam.append((name,height))

# print(footballTeam)

# def is_palindrome(number):
#     return str(number) == str(number)[::-1]

# palindrome_numbers = []

# for num in range(1, 1001):
#     if is_palindrome(num):
#         palindrome_numbers.append(num)

# print("Palindrome numbers in the first one thousand numbers:")
# print(palindrome_numbers)

# palindromeNumbers = []

# for i in range(0,1000):
#     if str(i) == str(i)[::-1]:
#         palindromeNumbers.append(i)

# print(palindromeNumbers)

sampleList =  [4,9,7,12,67,4,68,43,25,4,90,75]

uniqueList = []

for i in sampleList:
    if i not in uniqueList:
        uniqueList.append(i)

print(uniqueList)

