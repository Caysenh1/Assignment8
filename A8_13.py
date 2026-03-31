S1 = {1,2,3}
S2 = {4,5,6}
S3 = {1,3,5,7,9}
print(S1.difference(S3))
print(S1.intersection(S2))
print(S1.symmetric_difference(S3))
S4 = S1.union(S2)
print(S4.union(S3))
S1.add(4)
S1.add(5)
print(S1)
S2.remove(5)
print(S2)
