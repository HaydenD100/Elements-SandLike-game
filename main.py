#ID 
# Sand = 1
# Water = 2
# Wood = 3
#metal = 4
#lava = 5
#smoke = 6
#acid = 7
#fire
#Wood

import time
import pygame
import numpy as np
import math
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

PlaceId = 1

#id Lifetime EatTime
Grid = np.zeros((120,120,3))


WaterFlowRate = 5
LavaFlowRate = 3
Gravity = 2
FireLifeSpan = 200
FireEatTime = 4

WaterColors = [(3, 111, 252),(3, 123, 252),(3, 98, 252)]
LavaColors = [(252, 107, 3),(252, 78, 3),(252, 115, 3)]



def SetCircle(radius,x1,y1,id):
    x = 0
    while(x < 100):
        
        y = 0
        while(y < 100):
            if(math.sqrt((x - x1)**2 +(y -y1)**2) <= radius):
                Grid[x][y][0] = id
                if(id == 8):
                    Grid[x][y][1] = FireLifeSpan 
            y += 1
        x += 1
    
        

def Logic(id,x,y):


    
    if(id == 1): #Sand    
        if(y < 100 and Grid[x][y+1][0] in (0,2,5)):
            Grid[x][y][0] = Grid[x][y+1][0]
            Grid[x][y+1][0] = id + 0.1
            
                
        elif(x > 0 and y < 100 and Grid[x - 1][y+1][0] in (0,2,5)):
            Grid[x][y][0] = Grid[x - 1][y+1][0]
            Grid[x - 1][y+1][0] = id + 0.1
            
            
             
                
        elif(x < 100 and y < 100 and Grid[x + 1][y + 1][0] in (0,2,5)):
            Grid[x][y][0] = Grid[x + 1][y+1][0]
            Grid[x + 1][y+1][0] = id + 0.1
            
        else:
            Grid[x][y][0] = id
                       
    elif(id == 2): #Water
        if(y >= 99):
            Grid[x][y][0] = id
            
        elif(y < 100 and Grid[x][y+1][0] in (0,5,6)):
            if(Grid[x][y+1][0] == 5):
                Grid[x][y][0] = 6 + 0.1
            else:
                Grid[x][y][0] = Grid[x][y+1][0]
                Grid[x][y+1][0] = id + 0.1
                
                
        elif(x > 0 and y < 100 and Grid[x - 1][y+1][0] in (0,5)):
            if(Grid[x - 1][y+1][0] == 5):
                Grid[x][y][0] = 6 + 0.1
            else:
                Grid[x - 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
                
        elif(x < 100 and y < 100 and Grid[x + 1][y + 1][0] in (0,5)):
            if(Grid[x + 1][y + 1][0] == 5):
                Grid[x][y][0] = 6 + 0.1
            else:
                Grid[x + 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
            
            
        
        elif(x < 100 and Grid[x + 1][y][0] in (0,5)):
            if( Grid[x + WaterFlowRate][y][0] == 0):
                Grid[x + WaterFlowRate][y][0] = id + 0.1
                Grid[x][y] = 0
                
            else:
                if(Grid[x + 1][y][0] == 5):
                    Grid[x][y][0] = 6 + 0.1
                else:
                    Grid[x + 1][y][0] = id + 0.1
                    Grid[x][y][0] = 0

            
        elif(x > 0 and Grid[x - 1][y][0] in (0,5)):
            if( Grid[x - WaterFlowRate][y][0] == 0):
                Grid[x - WaterFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                Grid[x - 1][y][0] = id + 0.1
                Grid[x][y][0] = 0
       
        else:
            Grid[x][y][0] = id
          
    elif(id == 5): #Lava
        
        if(y >= 99):
            Grid[x][y][0] = id
            
        elif(y < 100 and Grid[x][y+1][0] in (0,2,3)):
            if(Grid[x][y+1][0] == 2):
                Grid[x+1][y][0] = 6 + 0.1
                
            elif(Grid[x][y+1][0] == 3):
                Grid[x][y+1][0] = id + 0.1
                Grid[x][y][0] = 6
                
            else:
                Grid[x][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
                
        elif(x > 0 and y < 100 and Grid[x - 1][y+1][0] in (0,2,3)):
            if(Grid[x - 1][y+1][0] == 2):
                Grid[x][y][0] = 6 + 0.1
                
            else:
                Grid[x - 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
                
        elif(x < 100 and y < 100 and Grid[x + 1][y + 1][0] in (0,2,3)):
            if(Grid[x + 1][y + 1][0] == 2):
                Grid[x][y][0] = 6 + 0.1
            else:
                Grid[x + 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
            
            
        
        elif(x < 100 and Grid[x + 1][y][0] in (0,2,3)):
            if( Grid[x + LavaFlowRate][y][0] == 0):
                Grid[x + WaterFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                if(Grid[x + 1][y + 1][0] == 2):
                    Grid[x][y][0] = 6 + 0.1
                else:
                    Grid[x + 1][y][0] = id + 0.1
                    Grid[x][y][0] = 0

            
        elif(x > 0 and Grid[x - 1][y][0] in (0,2,3)):
            if( Grid[x - LavaFlowRate][y][0] == 0):
                Grid[x - LavaFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                if(Grid[x + 1][y + 1][0] == 2):
                    Grid[x][y][0] = 6 + 0.1
                else:
                    Grid[x - 1][y][0] = id + 0.1
                    Grid[x][y][0] = 0
       
        else:
            Grid[x][y][0] = id

    elif(id == 6): #Smoke
        if(y <= 0):
            Grid[x][y][0] = id
            
        elif(y > 0 and Grid[x][y-1][0] in (0,1,5)):
            Grid[x][y-1][0] = id + 0.1
            Grid[x][y][0] = 0
                
        elif(x > 0 and y > 0 and Grid[x -1][y-1][0] in (0,1,5)):
            Grid[x - 1][y+1][0] = id + 0.1
            Grid[x][y][0] = 0
                
        elif(x < 100 and y > 0 and Grid[x + 1][y-1][0] in (0,1,5)):
            Grid[x + 1][y+1][0] = id + 0.1
            Grid[x][y][0] = 0
            
            
        
        elif(x < 100 and Grid[x + 1][y][0] == 0):
            if( Grid[x + WaterFlowRate][y][0] == 0):
                Grid[x + WaterFlowRate][y][0] = id
                Grid[x][y][0] = 0
                
            else:
                Grid[x + 1][y][0] = id + 0.1
                Grid[x][y][0] = 0

            
        elif(x > 0 and Grid[x - 1][y][0] == 0):
            if( Grid[x - WaterFlowRate][y][0] == 0):
                Grid[x - WaterFlowRate][y] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                Grid[x - 1][y][0] = id + 0.1
                Grid[x][y][0] = 0
       
        else:
            Grid[x][y][0] = id
            
    elif(id == 7): #Acid
        if(y >= 99):
            Grid[x][y][0] = id
            
        elif(y < 100 and Grid[x][y+1][0] in (0,4)):
                Grid[x][y][0] = 0
                Grid[x][y+1][0] = id + 0.1
                
                
        elif(x > 0 and y < 100 and Grid[x - 1][y+1][0] in (0,4)):

                Grid[x - 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
                
        elif(x < 100 and y < 100 and Grid[x + 1][y + 1][0] in (0,4)):

                Grid[x + 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
            
            
        
        elif(x < 100 and Grid[x + 1][y][0] in (0,4)):
            if( Grid[x + WaterFlowRate][y][0] == 0):
                Grid[x + WaterFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                Grid[x + 1][y][0] = id + 0.1
                Grid[x][y][0] = 0

            
        elif(x > 0 and Grid[x - 1][y][0] in (0,4)):
            if( Grid[x - WaterFlowRate][y][0] == 0):
                Grid[x - WaterFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                Grid[x - 1][y][0] = id + 0.1
                Grid[x][y][0] = 0
       
        else:
            Grid[x][y][0] = id
            
    elif(id == 8): #Fire
        Grid[x][y][1] = Grid[x][y][1] - 1
        if(Grid[x][y][1] <= 0):
            Grid[x][y][0] = 0
            return
        
        if(Grid[x][y][2] >= 1):
            Grid[x][y][2] = Grid[x][y][2] - 1
            
        if(Grid[x][y-1][0] == 0):
            Grid[x][y-1][0] = 6 + 0.1
        
        if(y >= 99):
            Grid[x][y][0] = id
                
        elif(y < 100 and Grid[x][y+1][0] in (0,2,3)):
            if(Grid[x][y+1][0] == 0):
                Grid[x][y+1][0] = id + 0.1
                
            if(Grid[x][y+1][0] == 0):
                Grid[x][y][0] = 0
                
            if(Grid[x][y+1][0] == 0):
                Grid[x][y][2] = FireEatTime
                Grid[x][y+1][0] = id + 0.1
                Grid[x][y+1][2] = FireEatTime
            

            
                
                
        elif(x > 0 and y < 100 and Grid[x - 1][y+1][0] in (0,3)):
            if(Grid[x - 1][y+1][0] == 0):
                Grid[x - 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
            
                
        elif(x < 100 and y < 100 and Grid[x + 1][y + 1][0] in (0,2,3)):
            Grid[x][y][1] = FireLifeSpan
            if(Grid[x + 1][y + 1][0] == 2):
                Grid[x][y][0] = 6 + 0.1
            else:
                Grid[x + 1][y+1][0] = id + 0.1
                Grid[x][y][0] = 0
            
            
        
        elif(x < 100 and Grid[x + 1][y][0] in (0,2,3)):
            Grid[x][y][1] = FireLifeSpan
            if( Grid[x + LavaFlowRate][y][0] == 0):
                Grid[x + WaterFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                if(Grid[x + 1][y + 1][0] == 2):
                    Grid[x][y][0] = 6 + 0.1
                else:
                    Grid[x + 1][y][0] = id + 0.1
                    Grid[x][y][0] = 0

            
        elif(x > 0 and Grid[x - 1][y][0] in (0,2,3)):
            Grid[x][y][1] = FireLifeSpan
            if( Grid[x - LavaFlowRate][y][0] == 0):
                Grid[x - LavaFlowRate][y][0] = id + 0.1
                Grid[x][y][0] = 0
                
            else:
                if(Grid[x + 1][y + 1][0] == 2):
                    Grid[x][y][0] = 6 + 0.1
                else:
                    Grid[x - 1][y][0] = id + 0.1
                    Grid[x][y][0] = 0
    
        else:
            Grid[x][y][0] = id


    


            
        
            
    
                
        
    



def draw():
    screen.fill((255, 255, 255))
    x = 0
    while(x < 100):
        
        y = 0
        while(y < 100 and x < 100): 
            if(Grid[x][y][0] == 1.0): #sand
                pygame.draw.rect(screen,(252, 173, 3),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 2.0): #water
                pygame.draw.rect(screen,random.choice(WaterColors),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 3.0): #wood
                pygame.draw.rect(screen,(48, 33, 0),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 4.0): #Metal
                pygame.draw.rect(screen,(43, 42, 38),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 5.0):#lava
                pygame.draw.rect(screen,random.choice(LavaColors),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 6.0):
                pygame.draw.rect(screen,(66, 66, 65, 20),(x * 6 ,y * 6 ,6,6))
                
            elif(Grid[x][y][0] == 7.0): #acid
                pygame.draw.rect(screen,(3, 161, 11),(x * 6 ,y * 6 ,6,6))
            elif(Grid[x][y][0] == 8.0):#fire
                pygame.draw.rect(screen,(255, 0, 11),(x * 6 ,y * 6 ,6,6))        
            y += 1
        x += 1
    
    pygame.display.update()
    
def Update():
    
    x = 0
    while(x < 100):
        
        y = 0
        while(y < 100):
            if(not Grid[x][y][0].is_integer()):
                Grid[x][y][0] -= 0.1
            else:
                Logic(Grid[x][y][0],x,y)
            y += 1
        x += 1
    

        
pygame.init()   

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

start_time = time.time()

FPSCounter = 0
seconds = 0

while running:
    
    FPSCounter = FPSCounter + 1
    current_time = time.time()
    if current_time - start_time >= seconds:
        seconds = seconds +1
        pygame.display.set_caption("FPS:" + str(FPSCounter))
        FPSCounter = 0
        


        
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = int(pos[0] / 6)
                y = int(pos[1] / 6)
                SetCircle(4,x,y,PlaceId)
            
            if event.type == pygame.K_1:
                PlaceId = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: #Sand
                    print("Sand")
                    PlaceId = 1
                
                elif event.key == pygame.K_2: #Water
                    print("Water")
                    PlaceId = 2  

                elif event.key == pygame.K_3: #Wood
                    print("Wood")
                    PlaceId = 3
                    
                elif event.key == pygame.K_4: #Metal
                    print("Metal")
                    PlaceId = 4
                    
                elif event.key == pygame.K_5: #Lava
                    print("Lava")
                    PlaceId = 5
                    
                elif event.key == pygame.K_6: #Smoke
                    print("Smoke")
                    PlaceId = 6
                    
                elif event.key == pygame.K_7: #Acid
                    print("Acid")
                    PlaceId = 7
                
                elif event.key == pygame.K_8: #Fire
                    print("Fire")
                    PlaceId = 8
                        
                
                
                
                               
    Update()
                
    draw()
    

