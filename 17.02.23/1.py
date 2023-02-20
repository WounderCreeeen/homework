def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;
    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d # чередование прироста 2 и 4: 5 + 2, 7 + 4, 11 + 2, и т.д.
    if prime == True:
        print(num)
a=2
while a<=100:
    is_prime(a)
    a+=1