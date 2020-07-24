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
                playerX -= 1
                print("LEFT")
            elif events.key == K_RIGHT:
                playerX += 1
                print("RIGHT")
                
    window.fill(Color("black"))
    #draw.line(window,Color("white"),UL,UR)
    #draw.line(window,Color("white"),UL,LL)
    #draw.line(window,Color("white"),LL,LR)
    #draw.line(window,Color("white"),UR,LR)
    
    

        
    
    draw.rect(window,Color("white"),(playerX,playerY,playerSizeX,playerSizeY))
    
    
    display.update()

