import time
import classes
from random import seed
st = time.time()
seed(48909)
screensize = 1200
main = classes.lifegamemain(eval(input("how many rows of cells? ")))
main.run()

print(time.time()-st)
