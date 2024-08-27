x=int(input())
for  i  in  range(x):
    lista=[]
    lista1=[]
    lista=list(map(int,input().split()))
    x=lista[0]
    y=lista[1]
    n=lista[2]
    lista1.append(x)
    for  i  in range(n-2):
        lista1.append(0)
    lista1.append(y)
    count=1
    for  j in  range((n-2),0,-1):
        if j+1<len(lista1):
            lista1[j]=lista1[j+1]-count
            count+=1
    if(lista1[1]-lista1[0])>(lista1[2]-lista1[1]):
        for i in  range(len(lista1)):
            print(lista1[i], end=" ")
    else:
        print(f'\n{-1}')