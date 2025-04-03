y=int(input("enter the 1 by performing incriment operater of somthing else for decriment "))
x = int(input("enter the value to get factorial"))
fact=1;
if(x==1):
    for i in range(1,x+1):
    fact=fact*i
    print(fact)
else:
    for i in range(x,1,-1):
    fact=fact*i
    print(fact)
