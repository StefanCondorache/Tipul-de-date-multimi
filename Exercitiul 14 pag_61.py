n=int(input('numarul de randuri: '))
matrice=[]
if n>=2 and n<=10:
    for i in range(n):
        matrice.append([])
    for i in matrice:
        print('randul',matrice.index(i)+1)
        for j in range(n):
            i.append(int(input('nuamrul: ')))
    sum1=0
    for i in range(n):
        sum1+=matrice[i][i]
    print('suma componentelor de pe diagonala principala: ',sum1)
    sum2,c=0,0
    for i in matrice[::-1]:
        sum2+=i[c]
        c+=1
    print('suma componentelor de pe diagonala secundara: ',sum2)
    sum3,sum4=0,0
    for i in range(n):
        for j in range(n):
            if i<j:
                sum3+=matrice[i][j]
            if i>j:
                sum4+=matrice[i][j]
    print('suma componentelor deasupra diagonalei principale: ',sum3)
    print('suma componentelor de sub diagonala principala: ',sum4)
    sum5,sum6=0,0
    for i in range(n):
        for j in range(n):
            if i+j<n-1:
                sum5+=matrice[i][j]
            if i+j>n-1:
                sum6+=matrice[i][j]
    print('suma componentelor deasupra diagonalei secundare: ',sum5)
    print('suma componentelor de sub diagonala secundara: ',sum6)