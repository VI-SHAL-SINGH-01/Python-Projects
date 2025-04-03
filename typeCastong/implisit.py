a=input("input the marks of 1st subject")
b=input("input the marks of 2nd subject")
c=input("input the marks of 3rd subject")
d=input("input the marks of 4th subject")
e=input("input the marks of 5th subject")

add = int(a) +int(b)+int(c)+int(d)+int(e)
per=add/500*100
if(per>=75):
    print("you are pass")   
else:
    print("Better luck next Time")
