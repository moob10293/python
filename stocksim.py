import random as r
import matplotlib.pyplot as plt
stocks=["vac","lrsk","dwj","apl"]
startingmoney=10_000

class stock:
    def __init__(self,name,cost,votality,votality2,dumbness,dumbness2,mainmarket,chance,chance2,ismain):
        '''
        name of stock, starting cost, how much a stock changes in thousandths percent, chance of ignoring move; 
        dumbness/dumbness2, closeness to major trend, chance of wining; chance/chance2
        '''
        tl=[]
        for x in range(chance):
            tl.append("win")
        for x in range(chance2-chance):
            tl.append("loose")
        self.win=r.choice(tl)
        
        self.dumbness=[]
        for x in range(dumbness):
            self.dumbness.append(True)
        for x in range(dumbness2-dumbness):
            self.dumbness.append(False)
        
        self.ismain=ismain
        if not ismain:
            self.mainmarket=[]
            for x in range(mainmarket-1):
                self.mainmarket.append(False)
            self.mainmarket.append(True)

        self.name=name
        self.cost=cost
        self.votality=votality
        self.votality2=votality2

    def day(self,mainmarket):

        if not self.ismain:
            follow=r.choice(self.mainmarket)
        else:
            follow=False
        if follow:
            direction=mainmarket
        else:
            direction=self.win
        dumb=r.choice(self.dumbness)

        if dumb:
            if direction:
                direction=False
            else:
                direction=True

        if self.win=="even":
            direction=r.choice([True,False])
        
        votality=r.randint(self.votality,self.votality2)
        move=votality*0.001*self.cost


        if not direction:
            move=0-move
        self.cost=self.cost+move

        print(f"{self.name} moved ${move} which is {votality*10}% and now has a price of {self.cost}")

    def recalc(self,win,loose,even):
        tl=[]
        for x in range(win):
            tl.append("win")
        for x in range(loose):
            tl.append("loose")
        for x in range(even):
            tl.append("even")
        self.win=r.choice(tl)

dowjones=stock("dwj",10_000,0,15,7,15,1,1,2,True)
vacine=stock("vac",10,10,100,)
prices=[teststock.cost]
days=[1]
plt.style.use("seaborn")
changechance=[False for x in range(49)]
changechance.append(True)
fig,ax=plt.subplots()
orders=[]

i="notno"
    while i !="no":
    for thestock in stocks:
        i=input("play?")
        if i=="showplot":
            ax.plot(days,prices,linewidth=5)
            plt.show()
            continue
        changewin=r.choice(changechance)
        if changewin:
            thestock.recalc(1,1,1)
        thestock.day("placeholder")
        prices.append(thestock.cost)
        days.append(days[-1]+1)
        while len(prices)>50:
            prices=prices[1:]
            days=days[1:]
#maingame:
'''
while True:
    for x in stocks:
        x.day()
    
    while True:
        order=input("what do you do?")
        if order=="sell":
            
        if order=="buy":

        if order=="sell short":
'''