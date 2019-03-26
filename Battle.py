def battle():
    t=int(input())
    for k in range(t):
        n=int(input())
        a=[int(x) for x in input().split()]
        d=[int(y) for y in input().split()]
        temp=0
        for i in range(n-1):
            if(d[i]>a[i-1]+a[i+1]):
                if(d[i]>temp):
                    temp=d[i]
        if(d[n-1]>a[0]+a[n-2]):
            if(d[n-1]>temp):
                temp=d[n-1]
        if(temp==0):
            print("-1")
        else:
            print(temp)


