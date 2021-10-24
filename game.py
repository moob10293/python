import pygame
import random
import time
pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
screen.fill((255, 255, 255))
pygame.display.set_caption("nothing")
screenrect = screen.get_rect()


class bullet:
    def __init__(self, lefttop):
        self.rect = pygame.Rect(lefttop[0], lefttop[1], 10, 5)

    def draw(self, move=False):
        if move:
            self.rect.x += move
        pygame.draw.rect(screen, (0, 0, 0), self.rect)


class enemy:
    def __init__(self, lefttop):
        self.rect = pygame.Rect(lefttop[0], lefttop[1], 20, 20)

    def draw(self, move, color):
        if move:
            self.rect.x += move
        pygame.draw.rect(screen, color, self.rect)


with open("gamescore.txt") as f:
    highscore = int(f.read())
bullets = []
enemies = []
blue = enemy((1100,random.randrange(100,700,21)))
green = enemy((1100,random.randrange(100,700,21)))
shoot = False
score = 0
yesblue = True
speed = 20
for y in range(100, 700, 21):
    enemies.append(enemy((1100, y)))
lastwave = time.time()
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"you lose, your score was {score}")
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            shoot = True
        if event.type == pygame.KEYUP:
            shoot = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
        if event.type == pygame.MOUSEBUTTONUP:
            shoot = False
    if shoot:
        bullets.append(bullet(pygame.mouse.get_pos()))
    for x in bullets:
        hit = False
        if x.rect.x > screen.get_size()[0]:
            hit = True
        for y in enemies:
            if x.rect.colliderect(y.rect):
                enemies.remove(y)
                score += 1
        if x.rect.colliderect(blue.rect):
            if yesblue:
                print(f"you lose, your score was {score} highscore is {highscore}")
                if highscore < score:
                    with open("gamescore.txt", "w") as f:
                        f.write(str(highscore))
                pygame.quit()
            else:
                blue = enemy((1100,random.randrange(100,700,21)))
                score += 1
        if x.rect.colliderect(green.rect):
            score += 1000
            green = enemy((1100,random.randrange(100,700,21)))
        if not hit:
            x.draw(15)
        else:
            bullets.remove(x)
    for x in enemies:
        x.draw(-speed,(255,0,0))
        if x.rect.x<0:
            enemies.remove(x)
    blue.draw(-speed,(0,0,255))
    green.draw(-speed,(0,255,0))
    if blue.rect.x<0:
        blue = enemy((1100,random.randrange(100,700,21)))
    if green.rect.x<0:
        green = enemy((1100,random.randrange(100,700,21)))
    if time.time() > lastwave + 1/(57*speed/20):
        for y in range(100, 700, 21):
            enemies.append(enemy((1100, y)))
        lastwave = time.time()
    pygame.display.flip()
    fps.tick(50)
