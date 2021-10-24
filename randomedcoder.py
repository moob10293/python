import random
message=input("enter the message: ")
dec=input('decode or encode: ')
numofcesar=eval(input('enter the key number'))
random.seed(a=numofcesar)
if dec=="decode":
    for x in message:
        print(chr(ord(x)-random.randint(0,150)),end='')
elif dec=="encode":
    for x in message:
        print(chr(ord(x)+random.randint(0,150)),end='')
else:
    while dec!="decode" and dec!="encode":
        print("that doesn't work")
        message=input("enter the message: ")
        dec=input('decode or encode: ')
        numofcesar=input('enter the key number')
        random.seed(a=numofcesar)
        print('enter only decode or uncode: ')
        if dec=="decode":
            for x in message:
                print(chr(ord(x)-random.randint(0,150)),end='')
        elif dec=="encode":
            for x in message:
                print(chr(ord(x)+random.randint(0,150)),end='')

