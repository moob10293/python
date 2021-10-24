import pickle
from plotly.graph_objs import Bar,Layout
from plotly import offline
import matplotlib.pyplot as plt
with open('ptverbsdictionary.pickle',"rb") as f:
    ptverbs = pickle.load(f)
xvalues = list(ptverbs.keys())
yvalues = list(ptverbs.values())

data = [Bar(x=xvalues,y=yvalues)]
xaxisconfig = {"title":"this is the x axis"}
yaxisconfig = {"title":"this is the y axis"}
layout = Layout(title = "a title",xaxis = xaxisconfig,yaxis = yaxisconfig)
offline.plot({"data":data,"layout":layout},filename = "graph.html")

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(15,9))
y_pos = range(len(xvalues))
ax.barh(y_pos, yvalues)
ax.set_yticks(y_pos)
ax.set_yticklabels(xvalues)
ax.invert_yaxis()
ax.set_xlabel('this is the x axis')
ax.set_ylabel('this is the y axis')
ax.set_title('a title')
plt.show()