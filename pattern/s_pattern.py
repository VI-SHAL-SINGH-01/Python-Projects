for x in range(0,7):
    for y in range(1,5):
        if(x==0 or x==6 or x==3):
            print("*",end="")
        elif(y==1 and ( x==1 or x==2) ):
            print("*",end="")
        elif(y==4 and (x==4 or x==5)):
            print("*",end="")       
        else:
            print(" ",end="")      
        
    print()
