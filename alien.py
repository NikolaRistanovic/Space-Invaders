import variables
class alienClass:
    
    
    def __init__(self):
        global aliensAlive
        aliensAlive = 4*[10*[True]]

    def isAlive(self,x,y):
        return aliensAlive[x][y]

    def kill(self,x,y):
        aliensAlive[x][y] = False
        for x in range(4):
            for y in range(10):
                if aliensAlive[x][y]:
                    global aliensDead
                    aliensDead += 1

    def shoot(self,x,y):
        pass

    def Render(self,Xoffset,Yoffset,x,y):
         posX = Xoffset + variables.L + (x*(variables.spaceing + variables.alienSizeX))
         posY = Yoffset + variables.U + (y*(variables.spaceing + variables.alienSizeY))
         return (posX,posY,variables.alienSizeX,variables.alienSizeY)