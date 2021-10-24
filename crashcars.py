import string, random, csv,math
import matplotlib.pyplot as plt
with open("cpdcrash.csv") as f:
    reader = csv.reader(f,delimiter=";")
    toprow = next(reader)
#    print(toprow)
    deaths = []
    car = []
 #   for index,name in enumerate(toprow):
 #       print(index,name)
    for x in reader:
        deaths.append(int(x[17]))
        car.append(x[46])

crashcars = []
totalcrashcars = []
for x in range(len(deaths)):
    pass
    if deaths[x] != 0:
        print(car[x],deaths[x])
        if not car[x] in crashcars:
            crashcars.append(car[x])
        totalcrashcars.append(car[x])
for x in crashcars:
    print(x,totalcrashcars.count(x)/car.count(x)*1000)