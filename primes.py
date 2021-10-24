import time
t=time.time()
l=[x for x in range(10_000_000)]
p=[2]
l.remove(0)
for x in l:
    prime=True
    for y in p:
        if y * y > x:
            break
        if x%y==0:
            prime=False
            break
    if prime:
        if x!=1:
            p.append(x)
print(p[-2:],time.time()-t)