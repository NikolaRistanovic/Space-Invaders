import variables
import alien



class playerClass:

    def shoot(self):
        if not(variables.projectileAlive):
                    (variables.projectileX,variables.projectileY) = (variables.playerX+(variables.playerSizeX//2)-(variables.projectileSizeX//2),variables.playerY)
                    variables.projectileAlive = True

    def left(self):
        if variables.playerX > variables.L:
                    variables.playerX -= 1

    def right(self):
        if variables.playerX + variables.playerSizeX <= variables.R:
                    variables.playerX += 1

    def goto(self,pos):
        if variables.playerX != pos:
            if pos > variables.playerX:
                playerClass.right(self)
            else:
                playerClass.left(self)

    def AI(self):
        if variables.aliensDead == 40:
            variables.AIstate = 6

        if variables.AIstate == 0 and not(variables.projectileAlive):
            variables.AIstate = 1


        variables.nextKill = variables.killOrder[variables.aliensDead]
        pos = alien.alienClass.Render(self,variables.offsetX,variables.offsetY,0,3)
        if (variables.AIstate == 1 and variables.nextKill[0]<2) or (variables.nextKill[0]>=2 and variables.nextKill[1]>=1):
            variables.dist[0] = ((variables.alienSizeX + variables.spaceing)*variables.nextKill[0])
            variables.dist[1] = ((variables.alienSizeY + variables.spaceing)*variables.nextKill[1])
            if pos[0] == 398 + variables.dist[0] - variables.dist[1] and variables.aliensDirection == 1:
                variables.AIstate = 2

        if variables.AIstate == 1 and variables.nextKill[0]>=2:
            variables.dist[0] = ((variables.alienSizeX + variables.spaceing)*variables.nextKill[0])
            variables.dist[1] = ((variables.alienSizeY + variables.spaceing)*variables.nextKill[1])
            if pos[0] == 550 - variables.dist[0] + variables.dist[1] and variables.aliensDirection == 0:
                variables.AIstate = 2

        if variables.AIstate == 2:
            check = True
            position1 = alien.alienClass.RenderWalls(self,0,2,2)
            position2 = alien.alienClass.RenderWalls(self,1,0,2)
            limit = alien.alienClass.RenderWalls(self,0,0,0)
            for i in range(variables.APsAlowed):
                if variables.APs[i][1] > limit[0]:
                    if variables.APs[i][0] >= position1[0]  + variables.wallSize and variables.APs[i][0] <= position2[0]:
                        check = False
            if check:
                variables.AIstate = 3

        if variables.AIstate == 3:
            position1 = alien.alienClass.RenderWalls(self,0,2,2)
            position2 = alien.alienClass.RenderWalls(self,1,0,2)
            distance = (position2[0] - (position1[0] + variables.wallSize) - variables.playerSizeX)//2
            position = position1[0] + variables.wallSize + distance
            playerClass.goto(self,position)
            if variables.playerX == position:
                variables.AIstate = 4
        
        if variables.AIstate == 4:
            playerClass.shoot(self)
            variables.AIstate = 5
        
        if variables.AIstate == 5:
            position1 = alien.alienClass.RenderWalls(self,0,0,2)
            position2 = alien.alienClass.RenderWalls(self,0,2,2)
            distance = ((position2[0] + variables.wallSize) - position1[0] - variables.playerSizeX)//2
            position = position1[0] + distance
            playerClass.goto(self,position)
            if variables.playerX == position:
                variables.AIstate = 0

        if variables.AIstate == 6:
            check = True
            for i in range(variables.APsAlowed):
                if variables.APisAlive[i]:
                    check = False
            if check:
                position = (variables.width - variables.playerSizeX) // 2
                playerClass.goto(self,position)

            