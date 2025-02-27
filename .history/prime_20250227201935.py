start=int(input('enter the starting number:'))
end=int(input('enter the last number:'))
for i in range(start,end+1):
    for j in range(2,(1//2)+1):
        if i%j==0:
            print(i)
    else:
        continue