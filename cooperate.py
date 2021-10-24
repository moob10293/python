import classes
main = classes.cooptmain()
while True:
    if input("continue? ") == "n":
        break
    else:
        main.go()