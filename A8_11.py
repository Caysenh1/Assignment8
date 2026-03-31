L = input("Enter integers: ")
L = L.split()
L = list(map(int, L))
M = max(L)
m = min(L)
I1 = L.index(M)
I2 = L.index(m)
L[I1], L[I2] = L[I2], L[I1]
print(*L)
