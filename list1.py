names = ["kamal", "jagath", "sunil", "ajith", "nimal"]

for index in range(0,len(names)):
    print(names[index],'is stored at index', index)

for name in names:
    print(name, 'is stored at index', names.index(name))
