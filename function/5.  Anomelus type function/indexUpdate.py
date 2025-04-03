''' reverse the 1st and last index of list objects '''

k=['hello','how','are','you']
s=[]
for i in k:
   list1=list(i)
   a=list1[0]
   list1[0]=i[-1]
   list1[-1]=a
   s="".join(list1)
   print(s,end=",")


'''conclusion : index of string can't be change it will give error that 
 Python, strings are immutable, so you can't change their characters in-place.
            
             i[0]=i[-1]
    TypeError: 'str' object does not support item assignment




'''