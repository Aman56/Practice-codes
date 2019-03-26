t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    lcm=a*b
    if(a<b):
        small=a
        big=b
    else:
        small=b
        big=a
    for j in range(1,small+1):
        if((a%j==0)and(b%j==0)):
            hcf=j
        if((big*j)%small==0):
            if(lcm>big*j):
                lcm=big*j
            

    print(hcf,lcm)
