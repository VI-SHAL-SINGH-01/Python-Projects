print('1.add')
print('2.subtract')
print('3.multiply')
print('4.devide')

x=int(input("enter your choice"))

if(1>=x<=4):
    a=int(input("input the first value"))
    b=int(input("input the second value"))
    if(x==1):
        print(a+b)
    elif(x==2):
        print(a-b)
    elif(x==3):
        print(a*b)
    elif(x==4):
        print(a/b)
else:
     print("out of range")
