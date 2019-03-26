"""t=int(input())
for i in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    r=[int(y) for y in input().split()]
    mul=1
    temp=0
    index=0
    for j in range(n):
        mul=l[j]*r[j]
        if(mul>temp):
            temp=l[j]*r[j]
            index=j+1
        if(mul==temp):
            if(r[j]>r[(index-1)]):
                index=j+1
            elif(r[j]==r[(index-1)]):
                if(j<index-1):
                    index=j+1
    print(index)

t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        a,b=map(int,input().split())
    h=0
    for j in range(1,n+1):
        h=h^j
    print(h)
    
t=int(input())
for i in range(t):
    n=int(input())
    d=[int(x) for x in input().split()]
    i=set(d)
    print(len(i))
"""
n=int(input())
if(n%4==0):
    n=n+1
else:
    n=n-1
print(n)
