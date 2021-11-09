x,y=int(input('numarul de elemente in multimea A:')),int(input('numarul de elemente in multimea B:'))
A={int(input('element in multimea A:')) for i in range(x)}
B={int(input('element in multimea B:')) for i in range(y)}
print('A:',A,'\nB:',B)
print('a)intersectia multimilor A si B:',A.intersection(B))
print('b)reuniunea multimilor A si B:',A.union(B))
print('c)diferenta multimilor A si B:',A.difference(B))