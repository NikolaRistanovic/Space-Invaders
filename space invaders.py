import pygame as pg
import sys
import alien
from variables import *



pg.init()
pg.display.set_caption("Space Invaders")
window = pg.display.set_mode((width,height))
pg.key.set_repeat(speed,speed)

aliens = alien.alienClass()

while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:      
            quit()
            sys.exit()
        elif events.type == pg.KEYDOWN:
            if events.key == pg.K_LEFT:
                if playerX > L:
                    playerX -= 2
                    print("LEFT")
            if events.key == pg.K_RIGHT:
                if playerX + playerSizeX <= R:
                    playerX += 2
                    print("RIGHT")
            if events.key == pg.K_UP:
                if not(projectileAlive):
                    print("FIRE")
                    (projectileX,projectileY) = (playerX+(playerSizeX//2)-(projectileSizeX//2),playerY)
                    projectileAlive = True
                
    window.fill(pg.Color("black"))
    pg.draw.line(window,pg.Color("white"),UL,UR)
    pg.draw.line(window,pg.Color("white"),UL,LL)
    pg.draw.line(window,pg.Color("white"),LL,LR)
    pg.draw.line(window,pg.Color("white"),UR,LR)
    
    pg.draw.rect(window,pg.Color("white"),(playerX,playerY,playerSizeX,playerSizeY))
    
    

    if projectileAlive:
        projectileY -= projectileSpeed
        pg.draw.rect(window,pg.Color("green"),(projectileX,projectileY,projectileSizeX,projectileSizeY))

    if projectileY <= U:
        projectileAlive = False
    
    for x in range(10):
        for y in range(4):
            pg.draw.rect(window,pg.Color("green"),aliens.Render(offserX,offsetY,x,y))

    pg.display.update()

