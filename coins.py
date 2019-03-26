def add(h):
    return(h*(h+1)/2)

t=int(input())
for i in range(t):
    n=int(input())
    h=1
    while(add(h)<=n):
        h=h+1
    print(h-1)

    
