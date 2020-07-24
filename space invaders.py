from pygame import *
import sys

#screen dimensions
(width,height) = (960,540)

#sides
(L,R,U,D) = (width//20,width-width//20,height//20,height-height//20)

#corners
#UpperLeft,UpperRight,LowerLeft,LowerRight
(UL,UR,LL,LR) = ((width//20,height//20),\
                 (width-width//20,height//20),\
                 (width//20,height-height//20),\
                 (width-width//20,height-height//20))

#player size
(playerSizeX,playerSizeY) = (69,54)

#player position
(playerX,playerY) = (L,D-playerSizeY)

#movement speed
speed = 10

#projectile size
(projectileSizeX,projectileSizeY) = (10,30)

#projectile position
(projectileX,projectileY) = (500,250)

#projectile speed
projectileSpeed = 2

#projectile state
projectileAlive = False



init()
display.set_caption("Space Invaders")
window = display.set_mode((width,height))
key.set_repeat(speed,speed)

while True:
    for events in event.get():
        if events.type == QUIT:      
            quit()
            sys.exit()
        elif events.type == KEYDOWN:
            if events.key == K_LEFT:
                if playerX > L:
                    playerX -= 1
                    print("LEFT")
            if events.key == K_RIGHT:
                if playerX + playerSizeX <= R:
                    playerX += 1
                    print("RIGHT")
            if events.key == K_UP:
                if not(projectileAlive):
                    print("FIRE")
                    (projectileX,projectileY) = (playerX+(playerSizeX//2)-(projectileSizeX//2),playerY)
                    projectileAlive = True
                
    window.fill(Color("black"))
    draw.line(window,Color("white"),UL,UR)
    draw.line(window,Color("white"),UL,LL)
    draw.line(window,Color("white"),LL,LR)
    draw.line(window,Color("white"),UR,LR)
    
    draw.rect(window,Color("white"),(playerX,playerY,playerSizeX,playerSizeY))
    
    

    if projectileAlive:
        projectileY -= projectileSpeed
        draw.rect(window,Color("green"),(projectileX,projectileY,projectileSizeX,projectileSizeY))

    if projectileY <= U-projectileSizeY:
        projectileAlive = False
    
    display.update()

