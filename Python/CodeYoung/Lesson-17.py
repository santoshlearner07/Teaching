listofSets= set()

while True:
    fruit = input("Enter fruit name")

    if fruit.lower == "done":
        break
    
    listofSets.add(fruit)

print(listofSets)

# unique_fruits = set()

# while True:
#     fruit = input("Enter a fruit (or 'done' to discontinue): ")
    
#     if fruit.lower() == 'done':
#         break
    
#     unique_fruits.add(fruit)

# print("\nUnique fruits entered:")
# for fruit in unique_fruits:
#     print(fruit)
