def nayi_hello(d):
    c=0
    #m=dict(itertools.combinations(d,2))
    #print(m)
    j=list(itertools.chain(itertools.combinations(d,2)))
    p=''.join(k)for k in j: if(set('aeiou').issubset(p)): c=c+1
    print(p)
    #if(set('aeiou').issubset(p)):
     #  c=c+1
    print(c)

def hello(t):
    for i in range(t):
        n=int(input())
        d=list(itertools.islice(sys.stdin,n))        
        print(d)
        nayi_hello(d)
import itertools,sys
def main():
    t=int(input())
    hello(t)
"""

import itertools,sys
t=int(input())
for i in range(t):
    n=int(input())
    d=list(itertools.islice(sys.stdin,n))
    c=0
    m=list(itertools.chain(itertools.combinations(d,2)))
    for k in m:
        p=''.join(k)       
        if(set('aeiou').issubset(p)):
           c=c+1
    print(c)


t=int(input())
for i in range(t):
    n=int(input())
    c=0
    s=0
    a=[int(x) for x in input().split()]
    for k in range(n):
        if(a[k]>0):
            c=c+1
        else:
            s=s+1
    if(c==0 and s!=0):
        print(s,s)
    elif(s==0 and c!=0):
        print(c,c)
    elif(c!=0 and s!=0):
        if(c>s):
            print(c,s)
        else:
            print(s,c)
        
t=int(input())
for i in range(t):
    n,d=map(float,input().split())
    p=float(str(n).lstrip(".0")+str(d).rstrip(".0"))
    big=0
    f=[]
    while(p!=0):
        f.append(int(p%10))
        p=int(p/10)
    f.reverse()
    
    for k in range(len(f)):
        if(f[k]>big):
            big=f[k]
            index=k
    f.remove(f[index])
    l=''.join(map(str,f))
    print(int(l))
"""
