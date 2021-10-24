equation=input("what is the equation?")
onnum=True
add=True
subtract=False
lon=[["+"]]
lon2=[]

for x in equation:

    if x == "+":
        onnum=False
        add=True
        lon.append(["+"])
    elif x == "-":
        onnum=False
        subtract=True
        lon.append(["-"])
    else:
        onnum=True

    if onnum:
        lon[-1:][0].append(x)

print(lon)

for x in lon:
    x.reverse()
    times=1
    number=0
    for y in x:

        try:
            y=int(y)
        except ValueError:
            if y=="-":
                number=-number
            lon2.append(number)
        else:
            number+=y*times
            times=times*10

print(lon2)

print(sum(lon2))