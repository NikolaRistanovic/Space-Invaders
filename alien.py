import variables
import random
class alienClass:
    
    
    
    def flockLimit(self):
        for y in range(10):
            for x in range(4):
                if variables.aliensAlive[x][y]:
                    variables.leftEdge = y * (variables.spaceing + variables.alienSizeX)
                    break
            else:
                continue
            break
        for y in range(9,-1,-1):
            for x in range(4):
                if variables.aliensAlive[x][y]:
                    variables.rightEdge = y * -(variables.spaceing + variables.alienSizeX)
                    break
            else:
                continue
            break

    def isAlive(self,x,y):
        return variables.aliensAlive[x][y]

    def isShooting(self,x,y):
        for i in range(5):
            if (x,y) == variables.aliensShooting[i]:
                return True
        return False


    def kill(self,x,y):
        variables.aliensAlive[x][y] = False
        variables.aliensDead += 1
        alienClass.flockLimit(self)
        variables.hadKill = True

    def shoot(self):
        for i in range(variables.APsAlowed):
            if variables.aliensDead < 40 and not(variables.APisAlive[i]):
                while 1:
                    (x,y) = random.randint(0,3),random.randint(0,9)
                    if alienClass.isAlive(self,x,y) and not(alienClass.isShooting(self,x,y)):
                        variables.APisAlive[i] = True
                        (posX,posY,AlienSizeX,alienSizeY) = alienClass.Render(self,variables.offsetX,variables.offsetY,y,x)
                        variables.APs[i] = (posX+AlienSizeX//2-variables.projectileSizeX//2,posY-variables.projectileSizeY)
                        break

    def Render(self,Xoffset,Yoffset,x,y):
         posX = Xoffset + variables.L + (x*(variables.spaceing + variables.alienSizeX))
         posY = Yoffset + variables.U + (y*(variables.spaceing + variables.alienSizeY))
         return (posX,posY,variables.alienSizeX,variables.alienSizeY)

    def colisionDetction(self,x,y):
        (posAX,posAY,sizeAX,sizeAY) = alienClass.Render(self,variables.offsetX,variables.offsetY,y,x)
        (posPX,posPY,sizePX,sizePY) = (variables.projectileX,variables.projectileY,variables.projectileSizeX,variables.projectileSizeY)
        if posAY + sizeAY >= posPY and posAY <= posPY - sizePY:
            if posAX + sizeAX >= posPX and posAX <= posPX - sizePX:
                alienClass.kill(self,x,y)
                variables.projectileAlive = False

    def hitDetection(self,iAP):
        if variables.APs[iAP][1] > variables.D - variables.playerSizeY - variables.projectileSizeY:
            if variables.playerX + variables.playerSizeX >= variables.APs[iAP][0] and variables.playerX <= variables.APs[iAP][0] - variables.projectileSizeX:
                variables.APisAlive[iAP] = False
                variables.playerState = 1

    def RenderWalls(self,s,x,y):
        posX = (variables.width//7)*(s+1)-(variables.wallSize+variables.wallSize//2)+variables.wallSize*x
        posY = variables.wallHeight + y*variables.wallSize
        return (posX,posY,variables.wallSize,variables.wallSize)

    def wallCollision(self):
        (posPX,posPY,sizePX,sizePY) = (variables.projectileX,variables.projectileY,variables.projectileSizeX,variables.projectileSizeY)
        for s in range(variables.wallNum):
            for x in range(3):
                for y in range(3):
                    (posWX,posWY,sizeWX,sizeWY) = alienClass.RenderWalls(self,s,y,x)
                    if posWY + sizeWY >= posPY and posWY <= posPY - sizePY:
                        if posWX + sizeWX >= posPX and posWX <= posPX - sizePX:
                            if variables.wallsState[s][x][y] > 0 and variables.projectileAlive:
                                variables.wallsState[s][x][y] -= 1
                                variables.projectileAlive = False
