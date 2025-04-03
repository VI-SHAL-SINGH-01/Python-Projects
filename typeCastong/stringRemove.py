a= [1, 2, 3, 'hello','string','hello','sum','run', 4, 3, 2]

b= []

for x in a:
    if x not in b:
        b.append(x)
a = b
print(f'Updated List after removing duplicates = {a}')
