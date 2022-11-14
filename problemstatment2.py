a=input()
res=[]
res4=[]
count=0
for i in a:
    if i.isdigit():
        res.append(i)
res=set(res)
res=list(res)
res1=sorted(res)
res2=res1[::-1]
res3="".join(res2)
res3=int(res3)
for i in res2:
    if(int(i)%2 != 0):
        count += 1
if(count==len(res2)):
    print(-1)
    exit(0)
if(res3%2==0):
    print(res3)
else:
    for i in res2:
        if(int(i)%2==0):
            res4.append(int(i))
    b=min(res4)
    c=res2.index(str(b))
    temp=res2[-1]
    res2[-1]=b
    res2[c]=temp
    res2=[str(i) for i in res2]
    res2=''.join(res2)
    print(int(res2))