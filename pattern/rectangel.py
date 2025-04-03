n= int(input("enter the no. of row"))
for i in range(n):
    for j in range(n-1):
        if(i==0 or j==0 or i==(n-1) or j==n-2 ):
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
