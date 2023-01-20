j=0
b=[]
while j<=3:
    a=int(input())
    b.append(a)
    j+=1
j=0
for i in b:
    if  i%2==0:
        j+=1
print(j)