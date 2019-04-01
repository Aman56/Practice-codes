t=int(input())
for i in range(t):
    n=int(input())
    q=n%12
    WS=[0,1,6,7]
    MS=[2,5,8,11]
    AS=[3,4,9,10]
    if(q in WS):
        s="WS"
        if(q==0):
            sn=n-11
        elif(q==1):
            sn=n+11
        elif(q==6):
            sn=n+1
        elif(q==7):
            sn=n-1
    elif(q in MS):
        s="MS"
        if(q==2):
            sn=n+9
        elif(q==5):
            sn=n+3
        elif(q==8):
            sn=n-3
        elif(q==11):
            sn=n-9      
    elif(q in AS):
        s="AS"
        if(q==3):
            sn=n+7
        elif(q==4):
            sn=n+5
        elif(q==9):
            sn=n-5
        elif(q==10):
            sn=n-7
    print(sn,s,sep=' ')
    
