

k=[5,"ravi", "shyam", "ram", "sumit", "ravi", "kavi", "shyam", "ravi","shyam"]
for i in k:
    c=0
    for j in k:
        if(i==j):
            c+=1
            if(c>1):
                k.remove(j)
print(k)

    




        
