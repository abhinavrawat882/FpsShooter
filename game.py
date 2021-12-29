from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import pygame
import numpy as np
import matplotlib.pyplot as plt
import math
import GameEnigneLib.AngleCal as ac
import GameEnigneLib.renderingFunctions as rf

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

    MapSize = [16, 16]

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
        rf.threDRenderer(plx, ply, pla, screen, mp, pygame)
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
