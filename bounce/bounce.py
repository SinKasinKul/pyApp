import sys
import time

import pygame

pygame.init()

size = width, height = 640, 480
dx = 1
dy = 1
dxx = 10
dyy = 10
x= 163
y = 120
xx= 163
yy = 120
black = (50,0,0)
white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = width -60
Y = height -20

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 16)

xx = 50
yy = 50

while 1:
    time.sleep(5/1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                if xx > 0 :
                    xx -= dxx

                if xx < 0 :
                    xx = 0
            elif (event.key == pygame.K_RIGHT):
                if xx < width :
                    xx += dxx

                if xx > width:   
                   xx = width
            elif (event.key == pygame.K_UP):
                if yy > 0 :
                    yy -= dyy

                if yy < 0 :
                    yy = 0
            elif (event.key == pygame.K_DOWN):
                if yy < height :
                    yy += dyy
                
                if yy > height:   
                   yy = height

    varTXY = "xx :" + str(xx) + "  yy :" + str(yy)
    text = font.render(varTXY, True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X , Y-20)

    varX = "x :" + str(x)
    varY = "y :" + str(y)
    text2 = font.render(varX + "---" + varY, True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (X, Y)

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx
        #time.sleep(1)

    if y < 0 or y > height:
        dy = -dy
        #time.sleep(1)

    #if yy < 0 or yy > height:
    #    dyy = -dyy

    #if x == xx :
    #     dx = -dxx
    #     dxx = -dx
    
    if y <= yy+2 :
        dy = -dy
    if x <= xx+2:
        dx = -dx
         
         #dyy = -dy

    screen.fill(black)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)

    pygame.draw.circle(screen, white, (x,y), 8)
    pygame.draw.circle(screen, white, (xx,yy), 8)


    pygame.display.flip()