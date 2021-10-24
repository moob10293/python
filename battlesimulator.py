import pygame,classes


class meleeperson:
    
    def __init__(self,damage,hp,speed,defense,direction,place,size,color=None):
        """a person (a square) that fights close range

        Args:
            damage (int): how much damage that person does
            hp (int): how much hp that person has
            speed (int): how much speed that person has
            defense (chance): (use my custom class) the chance of an enemy
            attack not doing damage
            direction (int): which direction the person is
            facing (the directions are 1,-1,2,-2 up,down,left,right respectively)
            place (tuple): a tuple with the left top cordinate of the person
            size (int): side length of the square
        """
        self.damage = damage
        self.hp = hp
        self.defense = defense
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(place[0],place[1],size,size)
        self.dead = False
        self.color = color

    def fightonce(self,otherperson):
        if self.direction == -otherperson.direction:
            if otherperson.defense.getchance():
                return
            else:
                otherperson.hp -= self.damage
                if otherperson.hp <= 0:
                    otherperson.dead = True
        else:
            otherperson.hp -= self.damage
            if otherperson.hp <= 0:
                otherperson.dead = True
            
    def move(self, turn = False, instant = False, distance = False):
        if turn:
            if turn == -self.direction:
                if classes.chance(self.speed,50).getchance() or instant:
                    self.direction = turn
                    return self.direction
                else:
                    return False
            else:
                if classes.chance(self.speed,100).getchance() or instant:
                    self.direction = turn
                    return self.direction
                else:
                    return False
        else:
            if distance:
                if abs(self.direction) == 1:
                    self.rect.y += self.speed * self.direction/-1
                elif abs(self.direction) == 2:
                    self.rect.x += self.speed * self.direction/-2
            else:
                if abs(self.direction) == 1:
                    self.rect.y += distance * self.direction/-1
                elif abs(self.direction) == 2:
                    self.rect.x += distance * self.direction/-2


class unit:
    
    def __init__(self,damage,hp,speed,defense,direction,size,length,width,spacing,left,top,color=None):
        self.listofpeople = []
        self.moral = 100
        self.surroundedsides = []
        for x in range(left,left+length*spacing,spacing):
            for y in range(top,top+width*spacing,spacing):
                self.listofpeople.append(meleeperson(damage,hp,speed,defense,direction,(x,y),size,color))

    def moveunit(self,enemy = []):
        try:
            if self.listofpeople[0].direction == -1 or self.listofpeople[0].direction == -2:
                self.listofpeople.reverse()
        except IndexError:
            return
        for x in self.listofpeople:
            move = True
            x.move(distance = attackdistance)
            for y in enemy:
                if x.rect.colliderect(y.rect):
                    x.fightonce(y)
                    move = False
            if move:
                z = self.listofpeople.copy()
                z.remove(x)
                x.move(distance = x.speed-attackdistance)
                for y in z:
                    if x.rect.colliderect(y.rect):
                        x.move(-x.direction,True)
                        x.move()
                        x.move(-x.direction,True)
            else:
                x.move(-x.direction,True)
                x.move(distance = attackdistance)
                x.move(-x.direction,True)
            pygame.draw.rect(screen,x.color,x.rect)
        if self.listofpeople[0].direction == -1 or self.listofpeople[0].direction == -2:
            self.listofpeople.reverse()

    def dieunits(self):
        for x in self.listofpeople:
            if x.dead == True:
                self.listofpeople.remove(x)

    def turnunit(self,direction):
        if self.listofpeople[0].move(direction,True):
            for x in self.listofpeople:
                x.direction = self.listofpeople[0].direction


pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((1200,1200))
screen.fill((255,255,255))
pygame.display.set_caption("battle simulator")
screenrect = screen.get_rect()
attackdistance = 2

a = unit(200,200,10,classes.chance(1,2),2,10,10,10,11,1000,100,(255,0,0))
b = unit(200,200,10,classes.chance(1,2),-2,10,10,10,11,100,100,(0,0,255))
lou = []#list of units
speed = 0
movecamera = False
xy = "x"
plusminus = "+"
cameraspeed = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                b.turnunit(1)
            if event.key == pygame.K_a:
                b.turnunit(2)
            if event.key == pygame.K_s:
                b.turnunit(-1)
            if event.key == pygame.K_d:
                b.turnunit(-2)
            if event.key == pygame.K_UP:
                movecamera = True
                xy = False
                plusminus = True
                for x in a.listofpeople:
                    x.rect.y += 50
                for y in b.listofpeople:
                    y.rect.y += 50
            if event.key == pygame.K_DOWN:
                movecamera = True
                xy = False
                plusminus = False
                for z in a.listofpeople:
                    z.rect.y -= 50
                for z in b.listofpeople:
                    z.rect.y -= 50
            if event.key == pygame.K_LEFT:
                movecamera = True
                xy = True
                plusminus = True
                for z in a.listofpeople:
                    z.rect.x += 50
                for z in b.listofpeople:
                    z.rect.x += 50
            if event.key == pygame.K_RIGHT:
                movecamera = True
                xy = True
                plusminus = False
                for z in a.listofpeople:
                    z.rect.x -= 50
                for z in b.listofpeople:
                    z.rect.x -= 50
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                speed = 1
            if event.key == pygame.K_2:
                speed = 10
            if event.key == pygame.K_0:
                speed = 5
            if event.key == pygame.K_3:
                speed = 50
            if event.key == pygame.K_UP:
                movecamera = False
            if event.key == pygame.K_DOWN:
                movecamera = False
            if event.key == pygame.K_LEFT:
                movecamera = False
            if event.key == pygame.K_RIGHT:
                movecamera = False
    if movecamera:
        if xy:
            if plusminus:
                for z in a.listofpeople:
                    z.rect.x += cameraspeed
                for z in b.listofpeople:
                    z.rect.x += cameraspeed
            else:
                for z in a.listofpeople:
                    z.rect.x -= cameraspeed
                for z in b.listofpeople:
                    z.rect.x -= cameraspeed
        else:
            if plusminus:
                for z in a.listofpeople:
                    z.rect.y += cameraspeed
                for z in b.listofpeople:
                    z.rect.y += cameraspeed
                
            else:
                for z in a.listofpeople:
                    z.rect.y -= cameraspeed
                for z in b.listofpeople:
                    z.rect.y -= cameraspeed
    if speed !=0:
        screen.fill((255,255,255))
        b.moveunit(a.listofpeople)
        a.moveunit(b.listofpeople)
        a.dieunits()
        b.dieunits()
        pygame.display.flip()
        fps.tick(speed)