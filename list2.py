names = ["kamal", "jagath", "sunil", "ajith", "nimal"]
print(names)

newIndexIn = input("enter the index to remove: ")
newIndex = int(newIndexIn)

newName = input("enter name to replace: ")

names[newIndex] = newName
print(names)

newName = input('enter a name to add: ')
names.append(newName)
print(names)

remName = input('enter a name to remove: ')
names.remove(remName)
print(names)

