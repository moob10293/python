import yfinance as yf

stock = yf.Ticker(input("what is the stock symbol? ").upper())
history = stock.history(period="6m")
closes = history["Close"]
prices = closes.to_numpy().tolist()

if len(prices) == 0:
    print("I don't think that stock exists")
else:
    print(sum(prices)/len(prices))