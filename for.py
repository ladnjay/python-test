numberIn = input('enter a number: ')
number = int(numberIn)

for test in range(2,number):

    if number % test == 0 and number != test:
        print(number,'equals', test, '*', number/test)
        prime = False
        break

else:
    print(number, 'is a prime number!')
