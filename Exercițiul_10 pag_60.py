A={1,2,3,4}
B=[[]]
for i in A:
    B+=[j + [i] for j in B]
print(B)