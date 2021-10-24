import pyautogui as p
import time
time.sleep(5)
p.PAUSE=0.02
n1=0
n2=0
n3=0
n4=0
lon=[0,1,2,3,4,5,6,7,8,9]
lon2=[6,7,8,9]
for a in lon:
    n1=a
    for b in lon:
        n2=b
        for c in lon:
            n3=c
            for d in lon:
                n4=d
                if n1*n2*n3*n4==12:
                    n1=str(n1)
                    n2=str(n2)
                    n3=str(n3)
                    n4=str(n4)
                    print(n1+n2+n3+n4)
                    n1=int(n1)
                    n2=int(n2)
                    n3=int(n3)
                    n4=int(n4)