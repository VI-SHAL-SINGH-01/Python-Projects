from os import remove

a= [ "hello","at", "ssb", "true" ,"try","at"]
for i in a:
    for j in i:
        if (((j == "a") or (j == "e") or (j == "i") or (j == "o") or (j == "u"))):
            #print(j,end=" ")
            a.remove(i)
            a.index(
            break
        else:
            continue
print(a,end=" ")
print(" ")
