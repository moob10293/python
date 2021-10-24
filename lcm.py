
num=eval(input("first number?"))
l=[]
while num != 0:
    l.append([num,{},1])
    num=eval(input("next number?"))
    '''
num2=eval(input("second number?"))
l1={}
l2={}
nat1=1
nat2=1
'''
while input("check another hundred?") != "no":
    for x in l:
        x[1].clear()
        for y in range(x[2],x[2]+1000):
            x[1][y*x[0]] = y
        x[2] = y

    '''
    l1.clear()
    l2.clear()
    for x in range(nat1,nat1+1000):
        l1[x*num1]=x
    nat1=x
    for x in range(nat2,nat2+1000):
        l2[x*num2]=x
    nat2=x
    '''
    for x in l[0][1].keys():
        for y in l[1][1].keys():
            for z in l[2][1].keys():
                if y==x==z:
                    print(y,l[0][1][x],l[1][1][y],l[2][1][z])
                    #print(f"the lcm is {y}, with times {l1[x]} for the first number and times {l2[y]} for the\nsecond number")

