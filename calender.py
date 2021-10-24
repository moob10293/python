import pygame,sys,time
auto=input("auto?")
if not auto:
    hours=0
    minutes=0
    seconds=1
    thing=input("what is the thing you want the alert for?")
else:
    hours=eval(input("how many hours does the timer take?"))
    minutes=eval(input("how many minutes does the timer take?"))
    seconds=eval(input("how many seconds does the timer take?"))
    thing=input("what is the thing you want the alert for?")
timetoaleart=hours*360+minutes*60+seconds

starttime=time.time()
while True:
    if starttime+timetoaleart<=time.time():
        pygame.init()
        screen=pygame.display.set_mode((2500,1300))
        screenrect=screen.get_rect()
        screen.fill((255,255,255))

        font=pygame.font.SysFont(None,300)
        enter="" if len(thing)>7 else f"{thing}!"
        enter2=f"{thing}!" if len(thing)>7 else ""

        image=font.render(f"time for {enter}",True,(0,0,0))
        imgrect=image.get_rect()
        imgrect.center=screenrect.center
        if not enter:
            imgrect.y-=300

        image2=font.render(f"{enter2}",True,(0,0,0))
        img2rect=image.get_rect()
        img2rect.center=screenrect.center
        for x in enter2:
            img2rect.x-=20
        img2rect.y+=300

        screen.blit(image,imgrect)
        screen.blit(image2,img2rect)
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            screen.blit(image,imgrect)
            screen.blit(image2,img2rect)
            pygame.display.flip()