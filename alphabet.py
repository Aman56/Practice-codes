s=input()
n=int(input())
w=[]

for i in range(n):
    w.append(input())
for k in w:
    f=0
    if(all (s) in k):
        f=1
    if(f==1):
        print("Yes")
    else:
        print("No")

