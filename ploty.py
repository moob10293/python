from plotly.graph_objs import Bar,Layout
from plotly import offline
import random
import matplotlib.pyplot as plt


class die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)




die1 =die()
die2 = die()
die3 = die()
results = [die1.roll()+die2.roll() for x in range(500000)]
max = die1.sides+die2.sides
numcounts = [results.count(x)for x in range(1,max+1)]
xvalues = list(range(1,max+1))

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(15,9))
y_pos = range(len(xvalues))
ax.barh(y_pos, numcounts)
ax.set_yticks(y_pos)
ax.set_yticklabels(xvalues)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('frequency of result')
ax.set_title('results of rolling 2 d6 50000 times')

plt.show()
'''
data = [Bar(x=xvalues,y=numcounts)]
xaxisconfig = {"title":"result"}
yaxisconfig = {"title":"frequency of result"}
layout = Layout(title = "results of rolling 2 d6 1000 times",xaxis = xaxisconfig,yaxis = yaxisconfig)
offline.plot({"data":data,"layout":layout},filename = "d6.html")
'''