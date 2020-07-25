import variables
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

    def kill(self,x,y):
        variables.aliensAlive[x][y] = False
        variables.aliensDead += 1
        alienClass.flockLimit(self)
        variables.hadKill = True

    def shoot(self,x,y):
        pass

    def Render(self,Xoffset,Yoffset,x,y):
         posX = Xoffset + variables.L + (x*(variables.spaceing + variables.alienSizeX))
         posY = Yoffset + variables.U + (y*(variables.spaceing + variables.alienSizeY))
         return (posX,posY,variables.alienSizeX,variables.alienSizeY)

    def colisionDetction(self,x,y):
        (posAX,posAY,sizeAX,sizeAY) = alienClass.Render(self,variables.offsetX,variables.offsetY,y,x)
        (posPX,posPY,sizePX,sizePY) = (variables.projectileX,variables.projectileY,variables.projectileSizeX,variables.projectileSizeY)
        if posAX + sizeAX >= posPX and posAX <= posPX - sizePX:
            if posAY + sizeAY >= posPY and posAY <= posPY - sizePY:
                alienClass.kill(self,x,y)
                variables.projectileAlive = False
        