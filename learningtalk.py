import random
dor={}
with open('responses.txt') as t:
    ts=t.read()
key=False
value=False
keys=[]
values=[]  
word=''
low=[]
index=0
for x in ts:
    if x=="\n":
        continue
    if x =="|":
        key=False
        keys.append(word)
        word=''
    if x=="-":
        value=False
        if low:
            low.append(word)
            values.append(low)
        else:
            values.append(word)
        word=''
        low=[]
    if x==',':
        value=False
        low.append(word)
        word=''
    if value:
        word+=x
    if key:
        word+=x
    if x==",":
        value=True
    if x ==";":
        key=True
    if x == ":":
        value=True
for x in range(len(keys)):
    dor[keys[x]]=values[x]
print('hello! talk to me, enter q or nothing to exit.')
i='placeholder'
r=''
while i!='q'and i!='':

    i=input('')

    if r:
        if dor.get(r,''):
            if type(dor[r])==str:
                dor[r]=[dor[r]]
            dor[r].append(i)
        else:
            dor[r]=i

    r=dor.get(i,i)

    if type(r)==list:
        r=random.choice(r)
        print(r)
    else:
        print(r)

dorwrite=''

for x,y in dor.items():

    if x=='\n' or y=='\n'or y=="q" or x=="q":
        continue

    x=f';{x}|'

    if type(y)==list:

        while '' in y:
            y.remove('')
        while "q" in y:
            y.remove("q")

        ty=''
        los=[]
        for z in y:
            if not z in los:
                ty+=f',{z}'
                los.append(z)

        y=ty[1:]
    y=f':{y}-'

    print(x,y)

    dorwrite+=f"{x}{y}\n"

with open('responses.txt','w') as t:
    t.write(dorwrite)