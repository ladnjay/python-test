userName = input('Enter your name: ')
userAge = input('Enter your age: ')
userFac = input('Enter a number: ')
#userFac = 5

finalName = userName + '!'

inAge = int(userAge) + int(userFac)
devAge = int(userAge) / int(userFac)
mulAge = int(userAge) * int(userFac)


print('Hello', finalName)

print('In', userFac, 'years you will be', inAge, 'years old')
print('Your age devided by', userFac, 'is', devAge)
print('Your age multiplied by', userFac, 'is', mulAge)
