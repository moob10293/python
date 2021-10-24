message=input("enter the encoded message: ")
counts = [message.count(c) for c in message]
maxletter=message[counts.index(max(counts))]
print('max char is(' + maxletter + ')')
try:
    print('the message is')
    for x in message:
        print(chr(ord(x)-(ord(maxletter)-32)),end='')

    print('\nor')

    for x in message:
        print(chr(ord(x)-(ord(maxletter)-101)),end='')

except ValueError:
    try:
        for x in message:
            print(chr(ord(x)-(ord(maxletter)-101)),end='')
    except ValueError:
        print("beep boop, overload, can't compute")
