l=input().split(',')
l=[int(i) for i in l]
for i in range(len(l)):
    if(l[i]==5):
        a=i
    if(l[i]==8):
        b=i
num1=sum(l[:a])+sum(l[b+1:])
l=[str(i) for i in l]
num2=int(''.join(l[a:b+1]))
print(num1+num2)