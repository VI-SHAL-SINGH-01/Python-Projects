k=[5000,45000,234000,234980]
v=[5] *len(k)
print('loop using map')
s=list(map(lambda x,y:x-(x*y/100),k,v))
print(s)
print('if else using map')
u=list(map(lambda x:x>10000 and x<10000000,k))
print(u)
#   it will print boolean values