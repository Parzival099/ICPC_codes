#https://codeforces.com/contest/2009/problem/B
x=int(input())
count=0
w=-1
for i in range(x):
    y=int(input())
    lista=[0]*y
    for j in range(y):
        z=input()
        for a in (z):
            if a=='#':
                lista[w]=count+1
                count=0
                w-=1
                break
            else:
                count+=1
    for p in lista:
        print(p,end=" ")
    print("")
    w=-1
    lista=[0]