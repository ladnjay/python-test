ages = {"kamal":35, "jagath":36, "sunil":38, "ajith":40, "nimal":30}
print(ages)

newKey = input('Enter key to change: ')
newValIn = input('Enter value to change: ')
newVal = int(newValIn)

ages[newKey] = newVal
print(ages)

newKey = input('Enter key to add: ')
newValIn = input('Enter value to add: ')
newVal = int(newValIn)

ages[newKey] = newVal
print(ages)

remKey = input('Enter key to remove: ')

del ages[remKey]
print(ages)
