###########################################
#       IMOPRT REQUIRED LIBRARY 
###########################################
GameResolution=[1280,720]
import pygame
from Assets import mainMenue
import game
import os
import time
###########################################
#      Load GAME SETTTINGS 
###########################################
gameFiles=os.listdir()
print(gameFiles)



# Import and initialize the pygame library
pygame.init()
screen = pygame.display.set_mode(GameResolution)
gameStack=['menue']
top=0
######################################
#      GAME  LOOP
######################################
while top>=0:
    if(gameStack[top]=='menue'):
        mainMenue.startMainMenue(pygame,screen,gameStack)
        print(gameStack)
        
    elif(gameStack[top]=='game'):
        settings=[]
        game.startGame(pygame,screen,gameStack,settings)
        time.sleep(0.3)
    top=len(gameStack)-1







