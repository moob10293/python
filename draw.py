import pygame,random
pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((1200,800))
screen.fill((255,255,255))
pygame.display.flip()
pygame.display.set_caption("nothing")
screenrect = screen.get_rect()


class pixel:
    def __init__(self,topleft):
        self.rect = pygame.Rect(topleft[0],topleft[1],5,5)
    def draw(self,move=False):
        pygame.draw.rect(screen,(0,0,0),self.rect)


pixels = []
draw = False
while True:
    #screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    if draw:
        pixels.append(pixel(pygame.mouse.get_pos()))
    for x in pixels:
        x.draw()
    pygame.display.update(pixels)