sum = 0
add = -1

while add !=0:
    print('The current sum is: ', sum)
    print('Enter to add:', end='')
    addIn = input('(Type 0 to exit):')
    add = int(addIn)
    sum = sum + add
