n=int(input())
c=bin(n)
c=c[2:]
print(c,type(c))
a=[]
b=0
for i in c:
    if int(i)==0:
        b=0
    if int(i)==1:
        b+=1
    if b>0:
        a.append(b)
print(max(a))
