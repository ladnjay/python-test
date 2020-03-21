name = input('Enter the name: ')
ageIn = input('Enter the age: ')

age = int(ageIn)

if age >= 21:
    print(name, 'you are allowed in!')
    print('You are also allowed to drink!')
elif age >= 18:
    print(name, 'you are allowd in but not to drink!')
else:
    print('Sorry', name, 'you are not allowd in!')
    
