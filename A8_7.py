names = input("Enter names: ")
names = names.split(', ')
names.sort()
a = names[0][0]
if a == "a" or a == "A":
    print(True)
else:
    print(False)

