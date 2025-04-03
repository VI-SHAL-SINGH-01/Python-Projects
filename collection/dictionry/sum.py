

s=34567
a=str(s)
k=[]
for i in a:
    k.append(i)
#k.pop(2)
k.reverse()
b=k[1]
k[1]=k[3]
k[3]=b

k=''.join(k)

print(k)