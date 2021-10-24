import matplotlib.pyplot as plt
import random
import plotly.express as px


class randomwalk:
    """a class to generate randomwalks"""
    def __init__(self, farness, numpoints = 5000):
        self.numpoints = numpoints
        self.xvalues = [0]
        self.yvalues = [0]
        self.farness = farness

    def fillwalk(self):
        while len(self.xvalues) < self.numpoints:
            xchange = random.choice([-1,1])*random.choice(range(1,self.farness + 1))
            ychange = random.choice([-1,1])*random.choice(range(1,self.farness + 1))
            self.xvalues.append(self.xvalues[-1]+xchange)
            self.yvalues.append(self.yvalues[-1]+ychange)


#xvalues = range(1,5001)
#yvalues = [x**3 for x in xvalues]
#fig = px.scatter(x=rw.xvalues, y=rw.yvalues)
#fig.show()

#plt.style.use("seaborn")
while True:
    rw = randomwalk(10,5000)
    rw.fillwalk()
    fig, ax = plt.subplots(figsize=(,9))
    pointnumbers = range(rw.numpoints)
    ax.scatter(rw.xvalues,rw.yvalues,c = pointnumbers,cmap=plt.cm.winter, edgecolors="none",s=15)
    #ax.plot(rw.xvalues,rw.yvalues,linewidth=1)
    ax.scatter(0,0,c="red",edgecolors="none",s=100)
    ax.scatter(rw.xvalues[-1],rw.yvalues[-1],c="black",edgecolors="none",s=100)
    plt.show()
#ax.scatter(xvalues,yvalues, c = yvalues,cmap=plt.cm.winter, s=300)
#ax.plot(inputvalues, squares, linewidth = 3)
#ax.set_title("square numbers", fontsize=24)
#ax.set_xlabel("value",fontsize=14)
#ax.set_ylabel("square of value",fontsize = 14)
#ax.tick_params(axis="both", which="major", labelsize = 14)
#ax.axis([0,6000,0,150000000000])
#plt.savefig("plot.png", bbox_inches = "tight")
#    plt.show()