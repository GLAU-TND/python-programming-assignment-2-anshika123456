ls=eval(input())
k=len(str(max(ls)))
ma=0
ans=""
l1=[]
print(ls)
ls=[str(i) for i in ls]
for h in range(len(ls)):
    ma=0
    for i in ls:
        for j in ls:
            if i!=j and i not in l1:
                y=i+j
                y=int(y[:k])
                if y>ma:
                   ma=y
                   n=str(i)
    l1.append(n)
for i in l1:
    ans=ans+i
print(ans)
