########################################
#        Library
########################################
import os
from pdb import pm
import time
from turtle import onscreenclick
#from LevelCreatorTool.OnScreenClasses import itemProp
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_0,
    K_9,
    K_a,
    K_z,

)
print( K_0,
    K_9)
print( K_a,
    K_z)
import OnScreenClasses
import DragAndDropCuntroler
import keyPressHandler
############################################
# GAME CONFIG
############################################
pygame.init()
mapResolution=[50,50]
mul=12
gameConfig = { 'font': pygame.font.SysFont(
    None, 24), 'itemListWidth': 130, 'pygame': pygame, 'itemPropHeight': 100,'currentOSIS':None,'Exit' : True}#current on screen item selected
gameConfig['GameResolution']=[gameConfig['itemListWidth']+mapResolution[0]*mul,gameConfig['itemPropHeight']+mapResolution[1]*mul]
gameConfig['mapResolution']=mapResolution
gameConfig['mul']=mul
############################################
# PYGAME INIT
############################################
screen = pygame.display.set_mode(gameConfig['GameResolution'])
############################################
# objects for on screen rendering
############################################
levelobj=None
itemProp=OnScreenClasses.itemProp(screen, gameConfig)
itemList = OnScreenClasses.itemList(screen, gameConfig)
levelEditor=OnScreenClasses.levelEditor(levelobj,(gameConfig['GameResolution'][0]-gameConfig['itemListWidth'],gameConfig['GameResolution'][1]-gameConfig['itemPropHeight']),gameConfig,itemProp)
MenueItems=OnScreenClasses.MenueItems(screen, gameConfig,levelEditor)
DNDC = DragAndDropCuntroler.cuntroler(screen, gameConfig, itemList,levelEditor,MenueItems)
kph=keyPressHandler.kph(levelEditor,itemList)
########################################
#        Code   Loop
########################################

t=time.time()
fps=0
pmpos=(0,0)
while gameConfig['Exit']:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameConfig['Exit']=False
    screen.fill((0, 0, 0))
    mousePos = pygame.mouse.get_pos()
    pressed_keys = pygame.key.get_pressed()
    x,y=pygame.mouse.get_pos()
    mouseActivity=pygame.mouse.get_pressed()  # MOUSE CLICK STATUS
    #print(mouseActivity)
    #######################
    #  ITEM LIST RENDERER
    #######################
    itemList.draw()
    ##########################
    #  ITEM PROPERTY RENDERER
    ##########################
    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(gameConfig['itemListWidth'], gameConfig['GameResolution'][1] -
                     gameConfig['itemPropHeight'], gameConfig['GameResolution'][0]-gameConfig['itemListWidth'], gameConfig['itemPropHeight']))
    txt = gameConfig['font'].render("ITEM PROPERTY", True, (0, 255, 255))
    screen.blit(txt, (gameConfig['itemListWidth']+10,
                gameConfig['GameResolution'][1]-gameConfig['itemPropHeight']+10))
    itemProp.draw()
    if MenueItems.draw():
        break
    ##########################
    # Drawing Main level mp
    ###########################
    levelEditor.draw(screen,gameConfig)
    #####################################
    # Drag and drop cuntroler
    #####################################
    screenObjectPressed=DNDC.dnds(mousePos, mouseActivity[0],pmpos)
    try:
        fps=1/(time.time()-t)
    except:
        fps=-1
    txt = gameConfig['font'].render(str(fps), True, (0, 255, 255))
    screen.blit(txt, (gameConfig['GameResolution'][0]-80,10))
    pygame.display.flip()
    t=time.time()
    pmpos=mousePos

