import pygame as pg
import sys
import alien
import variables as var
import player
import time



pg.init()
pg.display.set_caption("Space Invaders")
window = pg.display.set_mode((var.width,var.height))
pg.key.set_repeat(var.speed,var.speed)
textFont = pg.font.SysFont('Arial', 30)

aliens = alien.alienClass()
player = player.playerClass()
aliens.flockLimit()
textsurface = textFont.render(str(var.aliensDead), True, pg.Color("white"))
timeStart = round(time.time(),2)
timePrint = True
counter = 0
counterMax = 5
Display = False

while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:      
            quit()
            sys.exit()
        #--- elif events.type == pg.KEYDOWN: #obsolete because of AI
        #---     if events.key == pg.K_LEFT:
        #---         player.left()
        #---     if events.key == pg.K_RIGHT:
        #---         player.right()
        #---     if events.key == pg.K_UP:
        #---         player.shoot()
    if counter == counterMax:
        Display = True
        counter = 0
    else:
        Display = False
    if Display:
        window.fill(pg.Color("black"))
        pg.draw.line(window,pg.Color("white"),var.UL,var.UR)
        pg.draw.line(window,pg.Color("white"),var.UL,var.LL)
        pg.draw.line(window,pg.Color("white"),var.LL,var.LR)
        pg.draw.line(window,pg.Color("white"),var.UR,var.LR)
        
        pg.draw.rect(window,pg.Color(var.playerColor[var.playerState]),(var.playerX,var.playerY,var.playerSizeX,var.playerSizeY))

    if var.projectileAlive:
        var.projectileY -= var.projectileSpeed
        if Display:
            pg.draw.rect(window,pg.Color(var.playerColor[var.playerState]),(var.projectileX,var.projectileY,var.projectileSizeX,var.projectileSizeY))

    if var.projectileY <= var.U:
        var.projectileAlive = False

    
    for i in range(5):
        if var.APs[i][1] > var.D - var.projectileSizeY:
            var.APisAlive[i] = False

        if var.APisAlive[i]:
            (x,y) = var.APs[i]
            y += var.projectileSpeed
            var.APs[i] = (x,y)
            if Display:
                pg.draw.rect(window,pg.Color("green"),(x,y,var.projectileSizeX,var.projectileSizeY))
            aliens.hitDetection(i)

    
    if var.offsetX > var.R - var.L - (10 * var.alienSizeX + 9 * var.spaceing) - 405 - var.rightEdge:
        var.aliensDirection = 0
    if var.offsetX <= 0 - var.leftEdge:
        var.aliensDirection = 1
    
    if var.aliensDirection:
        var.offsetX += var.aliensSpeed
    else:
        var.offsetX -= var.aliensSpeed

    for x in range(4):
        for y in range(10):
            if var.projectileAlive:
                if aliens.isAlive(x,y):
                    aliens.colisionDetction(x,y)
            if Display:
                if aliens.isAlive(x,y):
                    pg.draw.rect(window,pg.Color("green"),aliens.Render(var.offsetX,var.offsetY,y,x))
    if Display:
        for s in range(var.wallNum):
            for x in range(3):
                for y in range(3):
                    if var.wallsState[s][y][x] > 0:
                        pg.draw.rect(window,pg.Color(var.wallsColor[var.wallsState[s][y][x]]),aliens.RenderWalls(s,x,y))

    if var.hadKill:
        textsurface = textFont.render(str(var.aliensDead), True, pg.Color("white"))
        var.hadKill = False
        if var.aliensDead < 40:
            var.APsAlowed = (var.aliensDead // 10) + 1

    if var.setup:
        position1 = aliens.RenderWalls(0,0,2)
        position2 = aliens.RenderWalls(0,2,2)
        distance = ((position2[0] + var.wallSize) - position1[0] - var.playerSizeX)//2
        position = position1[0] + distance
        player.goto(position)
        if var.playerX == position:
                var.setup = False
    if var.AIstate == 6 and timePrint:
        timeFinish = round(time.time(),2)
        print('Done in',round(timeFinish-timeStart,2),'seconds')
        timePrint = False
    aliens.shoot()
    aliens.wallCollision()
    if Display:
        window.blit(textsurface,(0,0))

    player.AI()
    if Display:
        pg.display.update()
    counter += 1
    #print(var.offsetY)
    #time.sleep(0.004)

