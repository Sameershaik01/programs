start=int(input())
end=int(input())
for i in range(start,end+1):
    bkp=i
    c=str(i)
    s=0
    for j in c:
        s+=int(j)**3
    if s==bkp:
        print(bkp)
    