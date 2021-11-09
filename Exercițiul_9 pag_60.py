x,y=int(input('numarul de elemente in multimea A:')),int(input('numarul de elemente in multimea B:'))
A,B=set(),set()
for i in range(x):
    a=str(input('element in multimea A:'))
    if a>='A' and a<='Z':
        A.add(a)
for i in range(y):
    a=str(input('element in multimea B:'))
    if a>='A' and a<='Z':
        B.add(a)
print('A:',A,'\nB:',B)
print('a)intersectia multimilor A si B:',A.intersection(B))
print('b)reuniunea multimilor A si B:',A.union(B))
print('c)diferenta multimilor A si B:',A.difference(B))