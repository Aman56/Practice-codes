t=int(input())
for i in range(t):
    n=int(input())
    temp=0
    a=[int(x) for x in input().split()]
    for j in a:
        if(j>temp):
            temp=j
    print(temp)
