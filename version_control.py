"""t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    c1=0
    c2=0
    for p in range(1,n+1):
        if(p in A and p in B):
            c1=c1+1
        elif(p not in A and p not in B):
            c2=c2+1
    print(c1,c2)

""" """
t=int(input())
for i in range(t):
    l=int(input())
    n=input()
    m=int(input())
    f=input()
    if(m>l):
        print("No")
    elif(m==l):
        if(n!=f):
            print("No")
    else:
    if(f in n):
        print("Yes")
    else:
        print("No")
"""

t=int(input())
for i in range(t):
    n=[int(input())]
    c=0
    d=0
    for k in n:
        print(k)
        if(k==1):
            c=c+1
        elif(k==0):
            d=d+1
    if(c==1 or d==1):
        print("Yes",c,d)
    else:
        print("No")
