#screen dimensions
(width,height) = (960,540)

#timer counter
counter = 3

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

#player color
playerColor = ["cyan","darkred"]

#player state
playerState = 0
setup = True

#movement speed
speed = 10

#projectile size
(projectileSizeX,projectileSizeY) = (5,15)

#projectile position
(projectileX,projectileY) = (width,height)

#projectile speed
projectileSpeed = 1

#projectile state
projectileAlive = False

#walls
wallsColor = ['black','darkred','red','white']
wallsState = [[[3,3,3] for _ in range(3)] for _ in range(6)]
wallSize = 30
wallHeight = height - 180
wallNum = 6


#alien size
(alienSizeX,alienSizeY) = (35,25)

#space between aliens
spaceing = 10

#screen offset for aliens
(offsetX,offsetY) = (20,20)

#flock edges
rightEdge = 0
leftEdge = 0

#number of dead aliens
aliensDead = 0
hadKill = False

#alien matrix
aliensAlive = [[True]*10 for _ in range(4)]

#direction of aliens
aliensDirection = 1

#speed of aliens
aliensSpeed = 1

#list of Alien projectiles
APsAlowed = 1
APs = [(0,0)] * 5
aliensShooting = (0,0) * 5
APisAlive = [False] * 5

#AI state of functioning
AIstate = 0
nextKill = [0,0]
dist = [0,0]
killOrder = [[0,0],[0,1],[0,2],\
            [1,0],[1,1],[1,2],[1,3],\
            [2,0],[2,1],[2,2],\
            [3,0],[3,1],[3,2],[3,3],\
            [0,3],\
            [4,0],[4,1],[4,2],\
            [5,0],[5,1],[5,2],[5,2],\
            [2,3],\
            [6,0],[6,1],[6,2],\
            [7,0],[7,1],[7,2],[7,3],\
            [4,3],\
            [8,0],[8,1],[8,2],[8,3],\
            [9,0],[9,1],[9,2],\
            [6,3],\
            [9,3],\
            [0,0]]