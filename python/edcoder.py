message=input("enter the message: ")
dec=input('decode or encode: ')
numofcesar=eval(input('enter a number to code it by: '))
if dec=="decode":
    for x in message:
        print(chr(ord(x)-numofcesar),end='')
elif dec=="encode":
    for x in message:
        print(chr(ord(x)+numofcesar),end='')
else:
    while dec!="decode" and dec!="uncode":
        print("that doesn't work")
        message=input("enter the message: ")
        dec=input('decode or encode: ')
        numofcesar=input('enter a number to code it by: ')
        print('enter only decode or uncode: ')
        if dec=="decode":
            for x in message:
                print(chr(ord(x)-numofcesar),end='')
        elif dec=="encode":
            for x in message:
                print(chr(ord(x)+numofcesar),end='')
