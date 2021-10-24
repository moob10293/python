import random
import turtle
import sys

mode=''
while mode!="easy"and mode!='medium'and mode!='hard':
    mode=input("Choose a mode, easy, medium, or hard: ")
    if mode=="easy":
        move=1
        size=200
        sea=300
    elif mode=="medium":
        move=40
        size=150
        sea=400
    elif mode=="hard":
        move=80
        size=100
        sea=500
    else:
        print("Sorry, that is not a mode.")

targetx=random.randint(0-sea,sea)
targety=random.randint(0-sea,sea)
targetx=500
targety=500
sizeofx=range(targetx,targetx+size)
sizeofy=range(targety,round(targety+(size/2)))

scor=0
tims=0
end=0
w=0
ycor=0
xcor=0

turtle.speed(0)
turtle.penup()
turtle.goto(0-sea,sea)
for x in range(4):
    turtle.pendown()
    turtle.forward(2*sea)
    turtle.right(90)
turtle.right(90)
turtle.penup()
turtle.home()

def maingame(x, y):
    turtle.speed(0)
    global size
    global move
    global targety
    global sizeofy
    global sizeofx
    global targetx
    global scor
    global tims
    global end
    global ycor
    global xcor
    if end!=1:
        turtle.goto(x,y)
        if turtle.xcor()!=xcor or turtle.ycor()!=ycor:
            if turtle.xcor() in sizeofx and turtle.ycor() in sizeofy and scor==9:
                turtle.color('grey')
                turtle.dot(20)
                tims=tims+1
                end=1
            elif turtle.xcor() in sizeofx and turtle.ycor() in sizeofy:
                turtle.color('grey')
                scor=scor+1
                turtle.dot(20)

                mov=True
                while mov:
                    xmovamount=random.randint(0-move,move)
                    ymoveamount=random.randint(0-move,move)
                    if -sea<targetx+xmovamount<sea and -sea<targety+ymoveamount<sea:
                        targetx=targetx+xmovamount
                        targety=targety+ymoveamount
                        sizeofx=range(targetx,targetx+size)
                        sizeofy=range(targety,round(targety+size/2))
                        mov=False

                tims=tims+1
                xcor=turtle.xcor()
            else:
                #print('cold')
                turtle.color('blue')
                tims=tims+1
                xcor=turtle.xcor()
                ycor=turtle.ycor()
            turtle.dot(20)
            print(targetx,targety)
    else:
        tims=str(tims)
        turtle.home()
        turtle.back(600)
        turtle.color('black')
        turtle.write("You win! You took "+tims+" trys to sink the enemy's ship",font=('arial',50,'bold'))

def cheatdraw():
    turtle.penup()
    turtle.goto(targetx,targety)
    turtle.pendown()
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.forward(200)

def cheathack(x,y):
    global end
    if end!=1:
        lon=[5,10,15,20,25]
        turtle.pu()
        turtle.goto(x,y)
        turtle.pd()
        for x in range(10):
            turtle.dot(20,'grey')
            turtle.right(random.randrange(360))
            turtle.pu()
            turtle.forward(random.choice(lon))
            turtle.pd()
        turtle.pu()
        turtle.home()
        turtle.back(600)
        turtle.color('black')
        turtle.pd()
        turtle.write("You win! You took 1 try to sink the enemy's ship",font=('arial',50,'bold'))
    end=1


#cheatdraw()
turtle.penup()
turtle.onscreenclick(fun=maingame, add=True)

if input("Press any key to exit ...") == "cheat":
    cheatdraw()
    input(" ")

