numberIn = input('enter a number: ')
number = int(numberIn)
test = 2

while test < number:
    if number % test == 0 and number != test:
        print(number,'equals', test, '*', number/test)
        print(number,'is not a prime number')
        break
    test = test + 1
else:
    print(number, 'is a prime number!')
