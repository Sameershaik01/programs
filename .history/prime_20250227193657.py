n=int(input('enter your number:'))
i=1
cnt=0
while i<=(n//2)+1:
    if n%i==0:
        cnt+=1
    i+=1
if cnt==1:
    print('prime')
else:
    print('not prime')