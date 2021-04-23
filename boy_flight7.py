import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((1300,1000))
clock = pygame.time.Clock()
background=pygame.image.load('road.gif')
rect=[0]*5
bbboy=[0]*4
bbboy1=[0]*4
bbboy_rot=[0]*4
bboy=[0]*4

angle=0
angle1=0
for m in range(4):
    name='bbboy'
    name0='bboy'
    m1=str(m)
    ext='.gif'
    bboy[m]=pygame.image.load(name0+m1+ext)
    bbboy[m]=pygame.image.load(name+m1+ext)
    bbboy1 [m]=pygame.transform.flip(bbboy[m],True,False)
image4=pygame.image.load('bbboy4.gif')

X,Y,Y2=200,700,200
i,i2,q=-1,-1,1
while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    i=i+1
    i1=i%4
    if Y>200:
        Y=Y-1
        rect[i1]=bboy[i1].get_rect(center=(X,Y))
        screen.blit(background,(0,0))
        screen.blit(bboy[i1],rect[i1])
        Y1=Y
    if Y<=200:
        i2=i2+1
        angle=angle+1
        if angle<30:
            bbboy_rot[i1]=pygame.transform.rotate(bbboy[i1],-angle)
            rect[i1]=bbboy_rot[i1].get_rect(center=(X,Y))
            screen.blit(bbboy_rot[i1],rect[i1])
        if angle>29:
            bbboy_rot[i1]=pygame.transform.rotate(bbboy[i1],-30)
            rect[i1]=bbboy_rot[i1].get_rect(center=(X,Y))
            screen.blit(bbboy_rot[i1],rect[i1])
            
            i3=i2%1600
            Y=Y1
            X=X+q*1
            if i3<800:
                q=1
                rect[i1]=bbboy_rot[i1].get_rect(center=(X,Y))
                screen.blit(background,(0,0))
                screen.blit(bbboy_rot[i1],rect[i1])
                #time.sleep(0.5)
            if i3>799:
                bbboy_rot[i1]=pygame.transform.rotate(bbboy1[i1],30)
                
                q=-1
                rect[i1]=bbboy_rot[i1].get_rect(center=(X,Y))
                screen.blit(background,(0,0))
                screen.blit(bbboy_rot[i1],rect[i1])
                X2=X
            if i2>=1800:
                q=1
                X2=372
                Y2=Y2+1
                if Y2>=750:
                    Y2=750
                
                angle1=angle1+1
                #print('angle1=',angle1)
                screen.blit(background,(0,0))
                if angle1<30:
                    bbboy_rot[i1]=pygame.transform.rotate(bbboy[i1],-30+angle1)
                    rect[i1]=bbboy_rot[i1].get_rect(center=(X2,Y2))
                    screen.blit(bbboy_rot[i1],rect[i1])
                    #time.sleep(1)
                if angle1>29:
                    rect[4]=image4.get_rect(center=(X2,Y2))
                    screen.blit(background,(0,0))
                    screen.blit(image4,rect[4])
    pygame.display.update()
    clock.tick(100)
    
