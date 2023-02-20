a=int(input())
b=int(input())
c=[]
d=[]
while a<=b:
    if a%2==0:
        c.append(a)
    else:
        d.append(a)
    a+=1
print(c)
print(d)