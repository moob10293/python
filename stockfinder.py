import yfinance as yf
import string, random, csv,math
import matplotlib.pyplot as plt
with open("stocknames.csv") as f:
    reader = csv.reader(f)
    toprow = next(reader)
    stocks = []
    for row in reader:
        stocks.append(row[0])
for x in stocks:
    if "^" in x:
        stocks[stocks.index(x)] = stocks[stocks.index(x)].replace("^","-P")
    if "/" in x:
        stocks[stocks.index(x)] = stocks[stocks.index(x)].replace("/","-")

prices = [10]
sortedprices = [800]
while 150<sortedprices[-1] or sortedprices[0]<1 or prices[-1]<prices[0]*1.5:
    stockname = random.choice(stocks)
    stock = yf.Ticker(stockname)
    history = stock.history(period="6mo")
    closes = history["Close"]
    prices = closes.to_numpy().tolist()
    if len(prices) < 100:
        continue
    sortedprices = prices.copy()
    sortedprices.sort()

print(1)
sortedprices = [x for x in sortedprices if not math.isnan(x)]
prices = [x for x in prices if not math.isnan(x)]
print(len(prices))
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(range(len(prices)),prices,linewidth = 2,color = "black")
print(2)
ax.set_title(stockname, fontsize=24)
print(sortedprices[0],sortedprices[-1],stockname)
ax.axis([0,130,sortedprices[0]*0.8,sortedprices[-1]*1.1])
print(3)
plt.show()
'''
except:
    try:
        print(stockname,sortedprices[:5],sortedprices[-5:],prices[:5],prices[-5:])
    except:
        print(stockname,sortedprices,prices)
'''