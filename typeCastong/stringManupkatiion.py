from operator import indexOf

    #remove the word which contain a,e,i,o,u

a= [ "hello","tries" ,"stand","at","at", "at", "ssb", "true" ,"try"]
for i in a:
    c=0
    for j in i:
        if (((j == "a") or (j == "e") or (j == "i") or (j == "o") or (j == "u"))):
            c+=1
            break
    if c > 0:
        a.remove(i)
        #del i
        #print(i,end=",")
print(a)
print(" ")