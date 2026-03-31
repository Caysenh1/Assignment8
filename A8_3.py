L1 = [1, 2, 3, 5, 7, 11, 13, 1, 2, 3]
L2 = ['Interstellar', 'The Martian', 'Apollo 13']
L3 = [1, 20, 15, 10, 5]
L4 = ['Bacon', 'Sausage', 'Steak']
L2.append('Star Wars')
print(L2)
print(L1.count(2))
print(L1+L2)
print(L1.index(3))
L4 = ['Chicken'] + L4
print(L4)
L3.remove(10)
L3.remove(20)
print(L3)
L3.reverse()
print(L3)
L3.sort()
print(L3)
L3.sort(reverse=True)
print(L3)
