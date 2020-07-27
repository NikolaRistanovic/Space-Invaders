import pygame as pg
import sys
import alien
import variables as var



pg.init()
pg.display.set_caption("Space Invaders")
window = pg.display.set_mode((var.width,var.height))
pg.key.set_repeat(var.speed,var.speed)
textFont = pg.font.SysFont('Arial', 30)

aliens = alien.alienClass()
aliens.flockLimit()
textsurface = textFont.render(str(var.aliensDead), True, pg.Color("white"))

while True:
    for events in pg.event.get():
        if events.type == pg.QUIT:      
            quit()
            sys.exit()
        elif events.type == pg.KEYDOWN:
            if events.key == pg.K_LEFT:
                if var.playerX > var.L:
                    var.playerX -= 2
            if events.key == pg.K_RIGHT:
                if var.playerX + var.playerSizeX <= var.R:
                    var.playerX += 2
            if events.key == pg.K_UP:
                if not(var.projectileAlive):
                    (var.projectileX,var.projectileY) = (var.playerX+(var.playerSizeX//2)-(var.projectileSizeX//2),var.playerY)
                    var.projectileAlive = True
                
    window.fill(pg.Color("black"))
    pg.draw.line(window,pg.Color("white"),var.UL,var.UR)
    pg.draw.line(window,pg.Color("white"),var.UL,var.LL)
    pg.draw.line(window,pg.Color("white"),var.LL,var.LR)
    pg.draw.line(window,pg.Color("white"),var.UR,var.LR)
    
    pg.draw.rect(window,pg.Color(var.playerColor[var.playerState]),(var.playerX,var.playerY,var.playerSizeX,var.playerSizeY))

    if var.projectileAlive:
        var.projectileY -= var.projectileSpeed
        pg.draw.rect(window,pg.Color(var.playerColor[var.playerState]),(var.projectileX,var.projectileY,var.projectileSizeX,var.projectileSizeY))

    if var.projectileY <= var.U:
        var.projectileAlive = False

    
    if var.APs[0][1] > var.D - var.projectileSizeY:
        var.APisAlive[0] = False

    if var.APisAlive[0]:
        (x,y) = var.APs[0]
        y += var.projectileSpeed
        var.APs[0] = (x,y)
        pg.draw.rect(window,pg.Color("green"),(x,y,var.projectileSizeX,var.projectileSizeY))

    
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

            if aliens.isAlive(x,y):
                pg.draw.rect(window,pg.Color("green"),aliens.Render(var.offsetX,var.offsetY,y,x))

    if var.hadKill:
        textsurface = textFont.render(str(var.aliensDead), True, pg.Color("white"))
        var.hadKill = False
    
    aliens.shoot()
    aliens.hitDetection(0)

    window.blit(textsurface,(0,0))

    pg.display.update()

