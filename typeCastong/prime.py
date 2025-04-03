k=[1,2,3,4,5,6,7,8,8,9,12,3,455,667,46]


for i in k:
   c=0
   for j in range(1,int(i/2+1)):
       if(i%j==0):
           c+=1
   if (c >= 2):
       print(i, end=" , ")
   else:
       print(i)


        
            
        
        
            
        
