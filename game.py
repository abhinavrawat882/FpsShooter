from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import cv2
import pygame
FOV=25
import math
import GameEnigneLib.AngleCal as ac
import GameEnigneLib.renderingFunctions as rf
gr=(1280,720)
######################
#INPUT EVENT HANDLER
######################
def update(pressed_keys, x, y, a,rd):
    run=True
    if pressed_keys[K_UP]:

        x += 0.01*math.cos(a*rd)
        y += 0.01*math.sin(a*rd)
    if pressed_keys[K_DOWN]:
        x -= 0.01*math.cos(a*rd)
        y -= 0.01*math.sin(a*rd)
    if pressed_keys[K_LEFT]:
        a += 2
    if pressed_keys[K_RIGHT]:
        a -= 2
    elif pressed_keys[K_ESCAPE]:
        run=False
    a = ac.giveAbsAngle(a)
    # print(a)
    return(x, y, a,run)


def startGame(pygame,screen,gameStack,settings):
    rd = 0.0174533

    plx = 12  # player position in x
    ply = 7  # player position in y
    pla = 0  # player view angle
    gnimg=pygame.image.load(r"C:\Users\abhin\Documents\Projects\FpsShooter\Assets\gun.png")
    gnimg = pygame.transform.scale(gnimg,( 190,160))
    MapSize = [16, 16]
    miniMapResolution=(48,48)
    mp = [[1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1., 1],
        [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1],
        [1, 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1],
        [1, 1., 1., 1., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1],
        [1, 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1],
        [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1],
        [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
        [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
        [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
        [1, 0., 1., 1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0, 1],
        [1, 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1],
        [1, 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1],
        [1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 0, 0., 1],
        [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1],
        [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1],
        [1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1., 1]]
    mp2=[[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
    ########################################
    # .          GAME LOOP
    #########################################
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ########################################
        # .          CLICK EVENT HANDLER
        #########################################
        pressed_keys = pygame.key.get_pressed()
        # print(pressed_keys)
        plx, ply, pla,running = update(pressed_keys, plx, ply, pla,rd)
        ########################################
        # .          DRAW ON SCREEN
        #########################################
        #print("ANGLE :",pla)
        # the background with white
        screen.fill((0, 0, 0))
        #ln,inter,xe,ye = rf.lineTracer(plx, ply, pla, mp)
        #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(gr[0]-miniMapResolution[0]-12,gr[1]-miniMapResolution[1]-10,miniMapResolution[0]+10,miniMapResolution[1]+10 ))
        #print(gr[0]-miniMapResolution[0]-12)
        rf.threDRenderer(plx, ply, pla, screen, mp, pygame,gr,FOV)
        screen.blit(gnimg,(gr[1]/2,(gr[0]-160)))
        rf.miniMapRenderer(screen, plx, ply, pla, pygame, mp,gr,miniMapResolution)
        #break

        ########################################
        # .          Heads up display
        #########################################

        #### HEALTH BAR




        ##### MINI MAP
        




        # Flip the display
        pygame.display.flip()

    if(running==False):
        gameStack.pop()
