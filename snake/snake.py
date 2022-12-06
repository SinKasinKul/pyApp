import time
import pygame
import random
import BallClaass
pygame.init()

size = width, height = 640, 480

mouseX = 0
mouseY = 0

ballsize = 20
rdx = 1
rdy = 1
gdx = 1
gdy = 1
bdx = 1
bdy = 1

dxx = ballsize/2
dyy = ballsize/2

black = (50,0,0)
white = (255,255,255)
blackRead = (50,0,0)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

pMouseX = 50
pMouseY = 10
tMouseX,tMouseY = "",""
vScore = 0

gx = random.randrange(0, width, 2)
gy = random.randrange(0, height, 2)

rx = random.randrange(0, width, 2)
ry = random.randrange(0, height, 2)

bx = random.randrange(0, width, 2)
by = random.randrange(0, height, 2)

screen = pygame.display.set_mode((size))
pygame.display.update()
pygame.display.set_caption('Snake game by Kasin')

font = pygame.font.Font('freesansbold.ttf', 16)


game_over=False
vT="MouseX : *** MouseY :***"

def ShowScore(vScore,x,y):
    score = font.render("Scores ::" + str(vScore), True, green, blue)
    scoreRect = score.get_rect()
    scoreRect.midleft = (x , y)

    return screen.blit(score, scoreRect)

def ShowText(vText,x,y):
    text = font.render(vText, True, green, blue)
    textRect = text.get_rect()
    textRect.midleft = (x, y)
    
    return screen.blit(text, textRect)

while not game_over:
    time.sleep(5/1000)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        elif event.type==pygame.MOUSEMOTION :
            mouseX, mouseY = pygame.mouse.get_pos()

            tMouseX = "MouseX :" + str(mouseX)
            tMouseY = "MouseY :" + str(mouseY)
            vT = tMouseX + " " + tMouseY
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_r):
                gx = random.randrange(0, width, 2)
                gy = random.randrange(0, height, 2)

                rx = random.randrange(0, width, 2)
                ry = random.randrange(0, height, 2)

                bx = random.randrange(0, width, 2)
                by = random.randrange(0, height, 2)
            elif (event.key == pygame.K_LEFT):
                if rx > 0 :
                    rdx -= rdx

                if rx < 0 :
                    rdx = 0
            elif (event.key == pygame.K_RIGHT):
                if rx < width :
                    rdx += rdx

                if rx > width:   
                   rdx = width + ballsize
            elif (event.key == pygame.K_UP):
                if ry > 0 :
                    rdy -= rdy

                if ry < 0 :
                    rdy = 0
            elif (event.key == pygame.K_DOWN):
                if ry < height :
                    rdy += rdy
                
                if ry > height:   
                   rdy = height + ballsize

            

        #print(event)   #prints out all the actions that take place on the screen

    #if (mouseX >= x-ballsize and mouseY >= y-ballsize) and (mouseX <= x+ballsize and mouseY <= y+ballsize) :
    #    x = random.randrange(0, width, 2) 
    #    y = random.randrange(0, height, 2) 
    vT2 = "Ball x:" + str(rx) + " y" + str(ry)
    screen.fill(blackRead)
    ShowText(vT,screen.get_width()-250 , pMouseY)
    ShowText("Scores ::" + str(vScore),0,pMouseY)
    ShowText(vT2,screen.get_width()-250 , pMouseY+50)
    #ShowScore(vScore,0,pMouseY)

    rx += rdx
    ry += rdy

    vr = random.randrange(-1, 0, 2)

    if (rx >= gx-ballsize and ry >= gy-ballsize) and (rx <= gx+ballsize and ry <= gy+ballsize)  and (rx <= bx-ballsize and ry <= by-ballsize):
        rdx = -rdx
        rdy = -rdy
        vScore = vScore + 1
    
    if rx <= 0 or rx >= width:   
        rdx = -rdx
    if ry <= 0 or ry >= height:
        rdy = -rdy

    gx += gdx
    gy += gdy

    if (gx >= rx-ballsize and gy >= ry-ballsize) and (gx <= rx+ballsize and gy <= ry+ballsize) and (gx <= bx+ballsize and gy <= by+ballsize):
        gdx = -gdx
        gdy = -gdy
        vScore = vScore + 1
    
    if gx <= 0 or gx >= width:   
        gdx = -gdx
        #time.sleep(1)

    if gy <= 0 or gy >= height:
        gdy = -gdy

    bx += bdx
    by += bdy

    if (bx >= rx-ballsize and by >= ry-ballsize) and (bx <= rx+ballsize and by <= ry+ballsize) and (bx <= rx+ballsize and by <= ry+ballsize):
        bdx = -bdx
        bdy = -bdy
        vScore = vScore + 1
    
    if bx <= 0 or bx >= width:   
        bdx = -bdx
        #time.sleep(1)

    if by <= 0 or by >= height:
        bdy = -bdy


    pygame.draw.circle(screen, green, (gx,gy), ballsize)
    pygame.draw.circle(screen, red, (rx,ry), ballsize)
    pygame.draw.circle(screen, blue, (bx,by), ballsize)
    pygame.display.flip()
 
pygame.quit()
quit()