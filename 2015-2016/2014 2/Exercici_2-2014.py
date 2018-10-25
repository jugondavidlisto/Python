n=input()
for i in range(1,n+1):
    seq=raw_input()
    ar=seq.split(" ")
    l=len(ar)
    res=0
    sume=0
    sumo=0
    for k in range(0,l):
        if k%2==0:
            sume+=int(ar[k])
        else:
            sumo+=int(ar[k])
    res=(sumo*3+sume)%10
    if res!=0:
        res=10-res
    print seq,res
