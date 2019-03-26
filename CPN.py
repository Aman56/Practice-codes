import itertools
import math
def muj():
    t=int(input())
    for i in range(t):
        s=input()
        if "MUJ" in s:
            print("YES")
        else:
            print("NO")
def empty():
    t=int(input())
    for i in range(t):
        n=int(input())
        cd={}
        for k in range(n):
            c,d=map(int,input().split())
            cd[c]=d
        l=list(itertools.chain(*sorted(cd.items())))
        c=2
        for k in range(1,len(l)-1,2):
            if(l[k]<l[k+1]):
                c+=1
        print(c)

def cmd():
    t=int(input())
    for i in range(t):
        n,q=map(int,input().split())
        a=[int(x) for x in input().split()]
        while(q):
            i_d,k=map(int,input().split())
            #a.remove(==i_d)
def sd():
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    for i in range(n-k+1):
        p=[]
        for j in range(k):
            p.append(a[i+j])
        add=sum(p)/k
        new_add=0
        for j in p:
            new_add+=math.pow(j-add,2)
        std=math.sqrt(new_add/k)
        print(std)
        
