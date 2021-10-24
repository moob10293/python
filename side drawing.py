import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
sides = eval(turtle.textinput("side amount","write amount of sides here"))
colors = ["red","blue","green","white","yellow","orange", "brown","pink","purple","grey","magenta","tan","cyan","olive",]
writing="I am sorry, a shape with that amount of sides does not exist"
if sides<=4 and sides>2:
    t.width(1)
elif sides==5:
    t.width(5)
elif sides<=2 or sides>len(colors):
    t.pu()
    t.right(180)
    t.fd(300)
    t.pd()
    t.pencolor("white")
    t.write(writing,font=("Arial", int(20),"bold"))
    raise SystemExit()
elif sides>10:
    t.width(15)
else:
    t.width(10)
for x in range(1000):
    t.pencolor(colors[x%sides])
    t.forward(x*0.8)
    t.left(360/sides + 1)
    
