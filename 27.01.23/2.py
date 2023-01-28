a=int(input())
b=int(input())
c=[]
if a==b:
    print('числа равны')
else:
    c.append(a)
    c.append(b)
    c.sort()
    print(c)