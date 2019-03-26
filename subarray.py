import math
def allSubArrays(my_list,k):
    subs = []
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            sub.sort()
            subs.append(sub*math.ceil((k/len(sub))))
            
            n += 1
    return subs

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=allSubArrays(a,k)
    
    print(b)
    x=b[k-1]
    ans=0
    for i in x:
        c=0
        if(i in b):
            c=c+1
        ans=ans+1
    if(ans!=0):
        print(ans)

