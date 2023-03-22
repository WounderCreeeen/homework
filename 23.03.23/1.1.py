a=input('текст')
b=input('искомый символ')
c=0
for i in a:
    if i==b:
        c+=1
print(f'символ {b} встречается в строке {a} {c} раз')