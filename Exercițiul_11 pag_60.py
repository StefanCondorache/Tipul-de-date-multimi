A={'A','B','C','D'}
B=[[]]
for i in A:
    B+=[j + [i] for j in B]
print(sorted(B))