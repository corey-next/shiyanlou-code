for i in range(1,101):
    if i%7==0:
        continue
    a=i
    while a%10!=7 and a!=0:
        a=int(a/10)
    if a!=0:
        continue
    print(i)
