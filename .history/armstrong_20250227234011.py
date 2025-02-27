n=int(input())
bkp=n
c=0
while n>0:
    t=n%10
    c+=t**3
    n=n//10
if c==bkp:
    print('armstrong')
else:
    print('not')