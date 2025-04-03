a=int(input("enter your first value"))
b=int(input("enter your second value"))
c= int(input("enter your third value"))

if(a>b & b >c):
   # print( a, " is greatest then" ,b ,"and greater then ", c)
   print(" x is gratest")
elif(a>b & b<c & c<a):
    #print( a, " is greatest then" ,c ,"and greater then ", b)
    print(" x is gratest")
elif(b>a & a>c):
   # print(b, " is greatest then" ,a ,"and greater then ", c)
   print(" y is gratest")
elif(b>a & a<c & b>c):
   # print( b, " is greatest then" ,c ,"and greater then ", a)
   print(" y is gratest")
elif(c>a & a>b):
    #print( c, " is greatest then" ,a ,"and greater then ", b)
    print(" y is gratest")
elif(c>a & a<b & c>b):
   # print( c, " is greatest then" ,b ,"and greater then ", a)
   print(" z is gratest")
elif(a<b<c):
    #print(c,"is greatest then",b,"and greater then",a)
    print(" z is gratest")
else:
    print(c, " is equal to", b, "and and also wqual to ", a)
