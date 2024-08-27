x=int(input())
lista=[]
count=0
for i in range(x):
    y=input()
    lista.append(y)
lista.sort(key=len)
for  i  in  range(x-1):
    if lista[i+1].find(lista[i])!=-1:
        count+=1
if count==x-1:
    print("YES")
    for  j  in  range(len(lista)):
        print(lista[j])
else:
    print("NO")