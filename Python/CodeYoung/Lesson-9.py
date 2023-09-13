# word = "hello"
# for letter in word:
#     print(letter)

# for i in range(6):
#     print(i)

# for i in range(5,25,3):
#     print(i)

# # que 1
sentence = "This is a sentene.This is a sentene.This is a sentene.This is a sentene.This is a sentene.This is a sentene.This is a sentene.This is a sentene.This is a sentene."
# for i in range(100):
#     print(sentence,i)
# x= 0
# for i in range(1000):
#     x = x + i

# print(x)
# # que 2
# text = 'Welcome to datagy! Here you will learn Python and data science.'
# print(len(text.split(" ")))

wordList = sentence.split()

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for word in wordList:
    vowelCount = 0
    for i in range(0, len(word)):
        if word[i] in vowels:
            vowelCount = vowelCount + 1

    print(vowelCount)


print(len(sentence.split(".")),"Number of sentence")
