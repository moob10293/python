import random
num=28.985
def fraccalc(num):
    whole=True
    decimal=False
    w=[]
    d=[]
    for x in f"{num}":
        if decimal:
            d.append(int(x))
        if x==".":
            decimal=True
            whole=False
        if whole:
            w.append(int(x))
    w.reverse()
    d.reverse()
    t=1
    wn=0
    for x in w:
        wn+=x*t
        t=t*10
    t=1
    dn=0
    for x in d:
        dn+=x*t
        t=t*10
    t=1
    lop=[]#list of probability
    for x in range(len(f"{dn}")):
        t=t*10
    for x in range(dn):
        lop.append(wn+1)
    for x in range(t-dn):
        lop.append(wn)
    return random.choice(lop)
l=[]
for x in range(100):
    l.append(fraccalc(num))
print(sum(l)/100,num)