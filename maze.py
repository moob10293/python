import random as r
import turtle as t
import pygame as p
import time
t.speed(0)
gridlength=1200
gridwidth=650
chanceofturning=10,11
chancelist=[]
movelist=[]

for x in range(chanceofturning[0]):
    chancelist.append(True)
for x in range(chanceofturning[1]-chanceofturning[0]):
    chancelist.append(False)

def move(turn=''):
    global lengthacross
    global widthacross
    if turn=='l':
        t.left(90)
        t.fd(50)
        t.right(90)
        widthacross+=50
    elif turn=='r':
        t.right(90)
        t.fd(50)
        t.left(90)
        widthacross-=50
    elif turn=='f':
        t.fd(50)
        lengthacross+=50
    elif turn=='b':
        t.fd(-50)
        lengthacross-=50
t.pu()
t.fd(-(gridlength/2))
t.pd()
t.left(90)
t.fd(gridwidth/2)
t.right(90)

for x in range(4):
    if x%2==0:
        t.fd(gridlength)
    else:
        t.fd(gridwidth)
    t.right(90)

startingpoint=r.randint(0,gridwidth/50)*50
t.pu()
t.goto(-(gridlength/2),-(gridwidth/2)+startingpoint)
t.pd()
lengthacross=0
widthacross=startingpoint
for x in range(5):
    while lengthacross != gridlength:  
        if widthacross>=gridwidth-50 and not (widthacross-50,lengthacross) in movelist: 
            mov='r'
        elif widthacross<=50 and not (widthacross+50,lengthacross) in movelist:
            mov='l'
        elif r.choice(chancelist) and not (widthacross-50,lengthacross) in movelist or not (widthacross+50,lengthacross) in movelist:
            mov=r.choice(('r','l'))
        elif not (widthacross,lengthacross+50) in movelist:
            mov='f'
        else:
            mov='b'
        move(mov)
        movelist.append((widthacross,lengthacross))
    t.pu()
    t.goto((-(gridlength/2))+50,-(gridwidth/2)+startingpoint)
    t.seth(0)
    t.pd()
    lengthacross=50
    widthacross=startingpoint
time.sleep(1)