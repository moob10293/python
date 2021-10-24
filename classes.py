from hashlib import new
import pygame
import sys
import random
import time

class chance:
    def __init__(self, val1, val2) -> None:
        self.chancelist = []
        self.val1 = val1
        self.val2 = val2
        for x in range(val1):
            self.chancelist.append(True)
        for x in range(val2-val1):
            self.chancelist.append(False)
    def getchance(self):
        if len(self.chancelist) != 0:
            return random.choice(self.chancelist)


class cell:
    def __init__(self, x, y, size, screen, los):
        self.screen = screen
        self.sizeofx = [n for n in range(x, x+size+1)]
        self.sizeofy = [n for n in range(y, y+size+1)]
        self.living = random.choice(los)
        self.celldrawing = pygame.Rect(x, y, size, size)
        co = (0, 0, 0) if self.living else (255, 255, 255)
        pygame.draw.rect(self.screen, co, self.celldrawing)
        self.last_living = 'placeholder'

    def draw_cell(self):
        if self.last_living == self.living:
            return
        co = (0, 0, 0) if self.living else (255, 255, 255)
        pygame.draw.rect(self.screen, co, self.celldrawing)
        self.last_living = self.living

    def determine(self, acn):
        if acn == 3:
            self.living = True
        elif acn > 3:
            self.living = False
        elif acn < 2:
            self.living = False


class grid:
    def __init__(self, cellrows, cellsize, screen, los):
        self.total_cells = cellrows**2
        self.celllist = []
        self.cellrows = cellrows
        self.cellsize = cellsize
        self.neighbors = {}
        self.lof = []
        for x in (1, 0, -1):
            for y in (1, 0, -1):
                self.lof.append((x, y))
        self.lof.remove((0, 0))
        for y in range(cellrows):
            y = y*self.cellsize
            for x in range(cellrows):
                x = x*self.cellsize
                self.celllist.append(cell(x, y, self.cellsize, screen, los))
        self.findneigbors()

    def findneigbors(self):
        self.nbrlbry = {}
        for ci in range(self.total_cells):
            nbrcs = []
            xoc = ci % self.cellrows
            yoc = ci//self.cellrows
            for y in self.lof:
                nx, ny = xoc+y[0], yoc+y[1]
                if self.cellrows > nx >= 0 and self.cellrows > ny >= 0:
                    idx = self.cellrows*ny + nx
                    nbrcs.append(idx)
            self.nbrlbry[ci] = nbrcs

    def draw(self):
        g = [x.living for x in self.celllist]
        for ci in range(self.total_cells):
            nbrcs = 0
            for x in self.nbrlbry[ci]:
                nbrcs += g[x]
            if nbrcs != 2:
                self.celllist[ci].determine(nbrcs)
            self.celllist[ci].draw_cell()
#        time.sleep(0.05)


class lifegamemain:
    def __init__(self, cellrows):
        self.cellrows = cellrows
        r = screensize % self.cellrows
        if r != 0:
            self.screensize = screensize+cellrows-r
        else:
            self.screensize = screensize
        self.cellsize = int(self.screensize/cellrows)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screensize, self.screensize))
        loggc = [[5, 1], [5, 2], [6, 1], [6, 2], [3, 13], [3, 14], [4, 12], [4, 16], [5, 11], [5, 17], [6, 11], [6, 15], [6, 17],
                 [6, 18], [7, 11], [7, 17], [8, 12], [8, 16], [9, 13], [9, 14], [
                     1, 25], [2, 23], [2, 25], [3, 21], [3, 22], [4, 21], [4, 22],
                 [5, 21], [5, 22], [6, 23], [6, 25], [7, 25], [3, 35], [3, 36], [4, 35],  [4, 36]]  # list of living glider gun cell cordinates
        glidergunindex = [self.cellrows*x[0]+x[1] for x in loggc]
        los = [False, False, False, False, False, False, True, True]
        g = grid(self.cellrows, self.cellsize, screen, los)
        computing = True
        clicked = False
        screen.fill((255, 255, 255))
        erase = False
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    sys.exit()
                if x.type == pygame.KEYUP:
                    if x.key == pygame.K_p:
                        if computing:
                            computing = False
                        else:
                            computing = True
                    elif x.key == pygame.K_c:
                        for y in g.celllist:
                            y.living = False
                            y.draw_cell()
                    elif x.key == pygame.K_f:
                        for y in g.celllist:
                            y.living = True
                            y.draw_cell()
                    elif x.key == pygame.K_g:
                        for y in glidergunindex:
                            g.celllist[y].living = True
                            g.celllist[y].draw_cell()
                if x.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    mx = pygame.mouse.get_pos()[0]
                    my = pygame.mouse.get_pos()[1]
                    for y in g.celllist:
                        if mx in y.sizeofx and my in y.sizeofy:
                            erase = True if y.living else False
                if x.type == pygame.MOUSEBUTTONUP:
                    clicked = False
                if clicked:
                    mx, my = pygame.mouse.get_pos(
                    )[0], pygame.mouse.get_pos()[1]
                    for y in g.celllist:
                        if mx in y.sizeofx and my in y.sizeofy:
                            y.living = False if erase else True
                        y.draw_cell()

            if computing:
                g.draw()
            pygame.display.flip()


screensize = 1200
size = 100


class picturemutatormain:
    def __init__(self):
        listofcolors = []
        for x in (255, 0):
            for y in (255, 0):
                for z in (255, 0):
                    listofcolors.append((x, y, z))
        pygame.init()
        self.screen = pygame.display.set_mode((screensize, screensize))
        startcolors = []
        for x in range(screensize**2):
            startcolors.append(random.choice(listofcolors))
        self.startpic = picture(self.screen, startcolors)

    def run(self):
        changechance = 1
        newchance = 0
        mutatefast = False
        #lastmutatetime = time.time()
        newpic=None
        while True:
            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    sys.exit()
                if x.type == pygame.KEYUP:
                    if x.key == pygame.K_1:
                        changechance = chance(1,100)
                    if x.key == pygame.K_2:
                        changechance = chance(50,100)
                    if x.key == pygame.K_3:
                        changechance = chance(100,100)
                    if x.key == pygame.K_4:
                        newchance = chance(0,100)
                    if x.key == pygame.K_5:
                        newchance = chance(1,100)
                    if x.key == pygame.K_6:
                        newchance = chance(100,100)
                    if x.key == pygame.K_SPACE:
                        mutatefast = False
                    if x.key == pygame.K_r:
                        newpic=picture(self.screen,self.startpic.mutate(changechance,newchance, True))
                        newpic.mutate(changechance, newchance)
                        print([x.color for x in newpic.listofpixels].count((0,0,255)))
                    if x.key == pygame.K_s and newpic:
                        self.startpic = newpic
                        newpic = None
                    if x.key == pygame.K_f:
                        for pi in self.startpic.listofpixels:
                            pi.color = (0,0,255)
                if x.type == pygame.KEYDOWN:
                    if x.key == pygame.K_SPACE:
                        mutatefast = True
            if mutatefast:# and time.time()-lastmutatetime > 0.2:
                self.startpic.mutate(changechance, newchance)
                newpic=None
                #lastmutatetime = time.time()
            if newpic != None:
                newpic.draw()
            else:
                self.startpic.draw()
            pygame.display.flip()


class picture:
    def __init__(self, screen, listofpixelcolors):
        self.pixelrows = screensize/size
        self.listofpixels = []
        pixelon = 0
        self.listofcolors = []
        for x in (255, 0):
            for y in (255, 0):
                for z in (255, 0):
                    self.listofcolors.append((x, y, z))
        for y in range(int(self.pixelrows)):
            y = y*size
            for x in range(int(self.pixelrows)):
                x = x*size
                self.listofpixels.append(
                    pixel(x, y, screen, listofpixelcolors[pixelon]))
                pixelon += 1
        self.lof = []
        for x in (1, 0, -1):
            for y in (1, 0, -1):
                self.lof.append((x, y))
        self.lof.remove((0, 0))
        self.nbrlbry = {}
        for pi in range(len(self.listofpixels)):
            nbrcs = []
            xoc = pi % self.pixelrows
            yoc = pi // self.pixelrows
            for y in self.lof:
                nx, ny = xoc+y[0], yoc+y[1]
                if self.pixelrows > nx >= 0 and self.pixelrows > ny >= 0:
                    nbrcs.append(
                        self.listofpixels[int(self.pixelrows*ny + nx)])
            self.nbrlbry[self.listofpixels[pi]] = nbrcs

    def mutate(self, changechance, newchance,copy=False):
        if not copy:
            for pix in self.listofpixels:
                if random.choice(changechance.getchance()):
                    pixchangecolors = []
                    if random.choice(newchance.getchance()):
                        pix.changecolor(random.choice(self.listofcolors))
                    else:
                        for x in self.nbrlbry[pix]:
                            pixchangecolors.append(x.color)
                        pix.changecolor(random.choice(pixchangecolors))
        else:
            copyof = self.listofpixels.copy()
            return [x.color for x in copyof]

    def draw(self):
        for pixel in self.listofpixels:
            pixel.draw()


class pixel:
    def __init__(self, x, y, screen, color):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)

    def changecolor(self, color):
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class person:
    def __init__(self,niceness):
        self.niceness = chance(niceness,10)
        self.points = 0
    def interact(self,otherperson):
        otherperson.interacted(self.niceness.getchance())
        self.interacted(otherperson.niceness.getchance())
    def interacted(self,othergood):
        selfgood = self.niceness.getchance()
        if selfgood:
            if othergood:
                self.points +=0
            else:
                self.points -= 2
        else:
            if othergood:
                self.points += 1
            else:
                self.points -=1
    def newgen(self,mutationchance):
        listofnewgen = []
        if self.points>0:
            for x in range(self.points):
                if mutationchance.getchance():
                    listofnewgen.append(person(random.randint(0,10)))
                else:
                    listofnewgen.append(person(self.niceness.val1))
        elif self.points == 0:
            listofnewgen.append(person(random.randint(0,10)))
        return listofnewgen
class cooptmain:
    def __init__(self):
        self.listofpeople=[]
        for x in range(90):
            self.listofpeople.append(person(10))
        for x in range(10):
            self.listofpeople.append(person(random.randint(0,10)))
        listofnicenesses = []
        for x in self.listofpeople:
            if x.niceness.val1 in listofnicenesses:
                pass
            else:
                print(f"amount of {x.niceness.val1} niceness people: {[y.niceness.val1 for y in self.listofpeople].count(x.niceness.val1)}")
                listofnicenesses.append(x.niceness.val1)
    def go(self):
        newpeople = []
        for x in self.listofpeople:
            for y in range(4):
                x.interact(random.choice(self.listofpeople))
        for x in self.listofpeople:
            newpeople += x.newgen(chance(1,15))
        self.listofpeople = newpeople
        listofnicenesses = []
        for x in self.listofpeople:
            if x.niceness.val1 in listofnicenesses:
                pass
            else:
                print(f"amount of {x.niceness.val1} niceness people: {[y.niceness.val1 for y in self.listofpeople].count(x.niceness.val1)}")
                listofnicenesses.append(x.niceness.val1)
        
        