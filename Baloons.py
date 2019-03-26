"""t=int(input())
for i in range(t):
    s=input()
    A=0
    B=0
    for j in s:
        if(j=='a'):
            A=A+1
        else:
            B=B+1
    if(A==0 or B==0):
        print("0")
    elif(A>B):
        print(B)
    else:
        print(A)

"""
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    
    if(m>n):
        small=n
    else:
        small=m
    hcf=1
    for j in range(1,small+1):
        if((m%j==0) and (n%j==0)):
            hcf=j
    print(int(m/hcf)*int(n/hcf))





t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    
    if(m>n):
        small=n
        big=m
    else:
        small=m
        big=n
    c=0
    while(small>0):
        temp=small
        small=big-small
        big=temp
        c=c+1
    print(c)
