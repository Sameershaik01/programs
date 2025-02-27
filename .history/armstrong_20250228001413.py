n=int(input())
s=str(n)
bkp=n
c=0
for i in s:
    c+=int(i)**3
if c==bkp:
    print('armstrong')
else:
    print('not')