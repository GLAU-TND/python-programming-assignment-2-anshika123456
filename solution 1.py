n=eval(input())
a=[]
p=n[0][-1]
a.append(n[0])
n=n[1:]
for j in n:
    for i in n:
        if p==i[0] and i not in a:
            a.append(i)
            p=i[-1]
print(a)
