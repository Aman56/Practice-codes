t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    for j in range(n):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
    print(a)
