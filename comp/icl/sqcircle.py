from math import sqrt
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    while(n!=0):
        n=n-(int(sqrt(n)))**2
        c+=1
    print(c)
