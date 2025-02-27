n=int(input('enter the number:'))
a=0
b=1
for i in range(1,(n-2)):
    c=a+b
    print(c)
    a=b
    b=c
