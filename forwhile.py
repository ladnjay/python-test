sum = 0
add = 10

for x in range(1,add):
    print('The current sum is: ', sum)
    print('Enter to add:', end='')
    addIn = input('(Type 0 to exit):')
    add = int(addIn)
    sum = sum + add
    x = 1
    if add == 0:
        break
