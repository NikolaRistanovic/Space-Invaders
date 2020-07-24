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
(projectileSizeX,projectileSizeY) = (5,15)

#projectile position
(projectileX,projectileY) = (0,0)

#projectile speed
projectileSpeed = 1

#projectile state
projectileAlive = False

#alien size
(alienSizeX,alienSizeY) = (35,25)

#space between aliens
spaceing = 10

#screen offset for aliens
(offserX,offsetY) = (20,20)
