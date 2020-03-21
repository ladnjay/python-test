numberIn = input('enter a number: ')
prime = True
number = int(numberIn)

for test in range(2,number):

    if number % test == 0 and number != test:
        print(number,'equals', test, '*', number/test)
        prime = False
        break

if prime:
    print(number, 'is a prime number!')
else:
    print(number, 'is not a prime number!')
