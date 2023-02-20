a=int(input())
b=int(input())
c=0
c1=[]
c2=[]
c3=[]

while a<=b:
    if a%2==0:
        c1.append(a)
    elif a%2!=0:
        c2.append(a)
    elif a%9==0:
        c3.append(a)
    a+=1
for i in c1:
    c=c+i
print(c)
for i in c2:
    c=c+i
print(c)
for i in c3:
    c=c+i
print(c)