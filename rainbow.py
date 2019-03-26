"""
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    f=0
    if(n%2!=0):
        mid=int(n/2)
        if(a[mid]==7):
            for k in range(1,mid):
                if(a[mid+k]!=a[mid-k]):
                    flag=1
    
    else:
        f=1
    if(f==1 or a[mid]!=7):
        print("no")
    else:
        print("yes")
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l=0
    p=0
    while(l<=a and p<=b):
        for i in range(1,min(a,b)):
            if(i%2!=0):
                l=l+i
            else:
                p=p+1
    if(l>a):
        print("Bob")
    elif(p>b):
        print("Limak")
