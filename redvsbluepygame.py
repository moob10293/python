import pygame as p
import sys,random,time
p.init()
screen=p.display.set_mode((1500,1200))
screen.fill((255,255,255))
screenrect=screen.get_rect()
bulletcooldown=0
blueimg=p.image.load('blue.png')
blueimgrect=blueimg.get_rect()
def bluespeed():
    return random.choice([1,0,2,1])
def fraccalc(num):
    if "." in f"{num}":
        whole=True
        decimal=False
        w=[]
        d=[]
        for x in f"{num}":
            if decimal:
                d.append(int(x))
            if x==".":
                decimal=True
                whole=False
            if whole:
                w.append(int(x))
        w.reverse()
        d.reverse()
        t=1
        wn=0
        for x in w:
            wn+=x*t
            t=t*10
        t=1
        dn=0
        for x in d:
            dn+=x*t
            t=t*10
        t=1
        lop=[]#list of probability
        for x in range(len(f"{dn}")):
            t=t*10
        for x in range(dn):
            lop.append(wn+1)
        for x in range(t-dn):
            lop.append(wn)
        return random.choice(lop)
    else:
        return num


class red:
    def __init__(self):
        self.image=p.image.load('red.png')
        self.rect=self.image.get_rect()
        self.rect.midleft=screenrect.midleft
    def draw(self):
        screen.blit(self.image,self.rect)


class blue:
    def __init__(self,y):
        self.rect=blueimg.get_rect()
        self.rect.right=screenrect.right
        self.side="placeholder"
        self.rect.y=y
        
    def shoot(self):
        if random.randint(1,1000)==1:
            bullets.append(bullet(blue,self.rect.center))

    def draw(self):
        self.rect.x-=fraccalc(0.25*bluespeed()) if slow else bluespeed()

        if random.randint(1,250)==1:
            self.side=random.choice(["up","down","placeholder"])
        if self.rect.top<=0 or self.rect.bottom>=screenrect.bottom:
            self.side=random.choice(["up","down","placeholder"])
        if self.side=="up":
                self.rect.y-=fraccalc(bluespeed()*0.25) if slow else bluespeed()
        elif self.side=="down":
            self.rect.y+=fraccalc(bluespeed()*0.25) if slow else bluespeed()

        self.shoot()
        screen.blit(blueimg,self.rect)


class bullet:
    def __init__(self,side,place=""):
        self.side=side
        if side=="red":
            self.rect=p.Rect(r.rect.left,r.rect.top,20,10)#10
            self.rect.center=r.rect.center
        else:
            self.rect=p.Rect(r.rect.left,r.rect.top,20,10)
            self.rect.center=place
    def shoot(self):
        if self.side=="red":
            self.rect.x+=fraccalc(0.25*3) if slow else 3
            p.draw.rect(screen,(255,0,0),self.rect)
        else:
            self.rect.x-=fraccalc(0.25*3) if slow else 3
            p.draw.rect(screen,(0,0,255),self.rect)

class aimer:
    def __init__(self):
        self.aimer=None
        pass

class score:
    def __init__(self):
        self.endfont=p.font.SysFont(None,150)
        self.normalfont=p.font.SysFont(None,50)
    def enddrawscore(self,score):
        score=f"You defeated {score} blues"
        scoreimage=self.endfont.render(score,True,(0,0,0))
        scorerect=scoreimage.get_rect()
        scorerect.center=screenrect.center
        screen.blit(scoreimage,scorerect)
    def drawnormalscore(self,score):
        score=str(score)
        scoreimage=self.normalfont.render(score,True,(0,0,0))
        scorerect=scoreimage.get_rect()
        scorerect.topright=screenrect.topright
        screen.blit(scoreimage,scorerect)
    def drawhighscore(self,score):
        score=f'highscore: {score}'
        scoreimage=self.normalfont.render(score,True,(0,0,0))
        scorerect=scoreimage.get_rect()
        scorerect.topleft=screenrect.topleft
        screen.blit(scoreimage,scorerect)

def drawgroup(screen,blue,bluelist,blueamount,spacebetween,blueimgrect):
    top=random.randint(0,screen.bottom-(blueamount*(blueimgrect.height+spacebetween)-spacebetween))
    for x in range(blueamount):
        bluelist.append(blue(x*blueimgrect.height+top+spacebetween*x))

with open('rvbhighscore.txt') as f:
    highscore=f.read()
highscore=int(highscore)

blueamount=5
spacebetween=25
s=score()
r=red()
movedown=False
moveup=False
bullets=[]
blues=[]
drawgroup(screenrect,blue,blues,blueamount,spacebetween,blueimgrect)
shoot=False
slow=False
rungame=True
bluedeaths=0
shootspeed=0.3


while True:

    screen.fill((255,255,255))

    for x in p.event.get():
        if x.type==p.QUIT:
            p.quit()
        elif x.type==p.KEYDOWN:
            if x.key==p.K_UP:
                moveup=True
            if x.key==p.K_DOWN:
                movedown=True
            if x.key==p.K_SPACE:
                shoot=True
            if x.key==p.K_p:
                bullets.clear()
                blues.clear()
                r.rect.midleft=screenrect.midleft
                bluedeaths=0
                rungame=True
            if x.key==p.K_z:
                slow=True
        elif x.type==p.KEYUP:
            if x.key==p.K_UP:
                moveup=False
            if x.key==p.K_SPACE:
                shoot=False
            elif x.key==p.K_DOWN:
                movedown=False
            if x.key==p.K_z:
                slow=False

    if rungame:
        if bluedeaths>highscore:
            highscore=bluedeaths
        if slow:
            shootspeed=1
        else:
            shootspeed=0.2
        if shoot:
            if time.time() >= bulletcooldown+shootspeed:
                bullets.append(bullet("red"))
                bulletcooldown=time.time()
        if movedown:
            if not r.rect.bottom>=screenrect.bottom:
                    r.rect.y+=fraccalc(2*0.25) if slow else 2
        if moveup:
            if not r.rect.top<=screenrect.top:
                    r.rect.y-=fraccalc(2*0.25) if slow else 2
        
        for b in blues:
            b.draw()
            if b.rect.left <= 0:
                blues.remove(b)
                if random.choice([1,0,0,0,0])==1:
                    drawgroup(screenrect,blue,blues,blueamount,spacebetween,blueimgrect)
            if b.rect.left==750:
                if random.choice([1,0,0,0,0])==1:
                    drawgroup(screenrect,blue,blues,blueamount,spacebetween,blueimgrect)
            if b.rect.colliderect(r.rect):
                rungame=False

        
        
        while len(blues)>=10:
            blues.pop(len(blues)-1)


        if len(blues)==0:
            drawgroup(screenrect,blue,blues,blueamount,spacebetween,blueimgrect)
        for bu in bullets:
            bu.shoot()
            if bu.side=="red":
                for b in blues:
                    if b.rect.colliderect(bu.rect):
                        bluedeaths+=1
                        blues.remove(b)
                        try:
                            bullets.remove(bu)
                        except ValueError:
                            pass
            else:
                if bu.rect.right<=screenrect.left:
                    bullets.remove(bu)
                if bu.rect.colliderect(r.rect):
                    rungame=False
                for buu in bullets:
                    if buu.side=="red":
                        if buu.rect.colliderect(bu.rect):
                            bullets.remove(buu)
                            bullets.remove(bu)


        s.drawhighscore(highscore)
        s.drawnormalscore(bluedeaths)
        r.draw()

    else:
        s.enddrawscore(bluedeaths)
        with open('rvbhighscore.txt','w') as f:
            f.write(str(highscore))

    p.display.update()