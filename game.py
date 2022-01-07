import time
import GameEnigneLib.preCalculations as pc
import GameEnigneLib.D3renderer as d3
import GameEnigneLib.D2Engine as d2
import GameEnigneLib.AngleCal as ac
import math
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)
import cv2
import pygame
FOV=25
import math
import GameEnigneLib.AngleCal as ac
import GameEnigneLib.D2Engine as d2
import GameEnigneLib.D3renderer as d3
import GameEnigneLib.lineTracer as lt
import GameEnigneLib.preCalculations as pc

playerSpeed=0.04
import time
import copy
import pygame
FOV = 25
gr = (1280, 720)
playerSpeed = 0.08


######################
# INPUT EVENT HANDLER
######################
def update(pressed_keys, x, y, a, ang, cs, si, noa, angStep, gtimer, gt):
    run = True
    if pressed_keys[K_UP]:

        x += playerSpeed*cs[ang]
        y += playerSpeed*si[ang]
    if pressed_keys[K_DOWN]:
        x -= playerSpeed*cs[ang]
        y -= playerSpeed*si[ang]
    if pressed_keys[K_LEFT]:
        a += angStep
        ang+=1
    if pressed_keys[K_RIGHT]:
        a -= angStep
        ang-=1
    if pressed_keys[K_SPACE] and gtimer==0:
        gt=time.time()
        gtimer=1
    
    
    
    if(ang>noa):
        ang=0
    elif(ang<0):
        ang=noa

    if pressed_keys[K_ESCAPE]:
        run=False
    a = ac.giveAbsAngle(a)
    # print(a)
    return(x, y, a, run, ang, gtimer, gt)


def startGame(pygame, screen, gameStack, levelData):
    #############################################################
    #                   LOAD GAME
    #############################################################

    angularStep=1
    plx = 12  # player position in x
    ply = 7  # player position in y
    pla = 0  # player view angle
    ang = 0

    # FIRST PERSON GUN IMAGES
    gnimg0 = pygame.image.load(
        r"Assets/Gun/gun.png")
    gnimg1 = pygame.image.load(
        r"Assets/Gun/gun1.png")
    gnimg2 = pygame.image.load(
        r"Assets/Gun/gun2.png")
    gnimg3 = pygame.image.load(
        r"Assets/Gun/gun3.png")
    gnimg = []
    gnimg.append(gnimg0)
    gnimg.append(gnimg1)
    gnimg.append(gnimg2)
    gnimg.append(gnimg3)

    # GUN IMAGE ON SCREEN
    gt = 0


    ## ENEMY IMAGES####
    enemyWalking = pygame.image.load(r"Assets/Enemy/enemyW.png")

    enemyShooting = pygame.image.load(r"Assets/Gun/gun1.png")
    enemyWalking = pygame.transform.scale(enemyWalking, (400,720))
    ewr=(400,720)

    ############################




    # PRECALCULATE VARIABLES
    gunLocation = (gr[0]/2+30, gr[1]-230)
    cs, si, noa, angleBeetweenLines, lineAngle, dy, dx, llpy, llpx,d3angularStep = pc.calc(
        FOV, pla, angularStep, gr)
    MapSize = [16, 16]
    miniMapResolution = (48, 48)
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
    #  enemyList Template
    #  [TypeOfEnemy ,x,y,health,time of death]
    enemyList=[[1,7,2,50,-1],[1,13,9,50,-1],[1,10,6,50,-1],[1,10,11,50,-1],[1,5,2,50,-1]]
    # This is a list of enemy's each element in the list is enemy template giving info about the enemy

    gtimer = 0
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
        plx, ply, pla, running, ang, gtimer, gt = update(
            pressed_keys, plx, ply, pla, ang, cs, si, noa, angularStep, gtimer, gt)

        ########################################
        # .          DRAW ON SCREEN
        #########################################
        # the background with white
        screen.fill((0, 0, 0))
        
        ##Draw the main seen
        d3.threDRenderer(plx, ply, screen,pygame,gr,lineAngle,angleBeetweenLines,ang,dy,dx,llpy,llpx,mp)
        
        ###############################
        #Now On TOP OF SEEN DRAW ENEMY
        ###############################
        
        #for enemy in enemyList:
        #    #  enemyList Template
        #    #  [0: TypeOfEnemy ,1: x,2: y,3 : health,4 :time of death]
        #    
        #    Ene_ply_ang=math.tanh(abs(ply-enemy[2])/abs(plx-enemy[1]))
        #    
        #    la=ac.giveAbsAngle(Ene_ply_ang*180/math.pi)
        #    ea=ac.giveAbsAngle(pla-FOV)
        #    sa=ac.giveAbsAngle(pla+FOV)
        #    doIt=0
        #    if(sa>=0 and ea<360 and sa <90 and ea>270):
        #        if la<sa or la>ea:
        #            doIt=1
        #    else:
        #        if la<sa and la>ea:
        #            doIt=1
        #        
        #    if(doIt==1):
        #        dist_ene_player=((plx-enemy[1])**2 + (ply-enemy[2])**2)**(0.5)
        #        edy=(math.sin(la*math.pi/180))
        #        edx=(math.cos(la*math.pi/180))
        #        ellpy=(abs( 1/math.sin(la*math.pi/180)))
        #        ellpx=(abs(1/math.cos(la*math.pi/180)))
        #        ln,inter,xe,ye=lt.lineTracer(plx, ply,la, mp, edy,edx,ellpy,ellpx)
        #        ss=abs(sa-la)
        #        es=abs(ea-la)
        #        sc=0
        #        
        #        ewrc=[ewr[0],ewr[1]]
        #        ewrc[0]/=ln
        #        ewrc[1]/=ln
        #        enemyWalkingc = pygame.transform.scale(enemyWalking,ewrc )
        #        if(ss<es):
        #            sc=ss*(1/d3angularStep)-ewr[0]/2
        #        else:
        #            sc=gr[0]-es*(1/d3angularStep)-ewrc[0]/2
        #        screen.blit(enemyWalkingc,(sc,(gr[1]/2)-(ewrc[1]/2)))


        #NEXT LAYER IS GUN 
        if(gtimer==1):
            if(time.time()-gt>0.9):
                gtimer=0
                screen.blit(gnimg[0],(gunLocation))
                
            elif(time.time()-gt>0.6):
                screen.blit(gnimg[3],(gunLocation))
            elif(time.time()-gt>0.3):
                screen.blit(gnimg[2],(gunLocation))
            else:    
                screen.blit(gnimg[1],(gunLocation))
        else:
            screen.blit(gnimg[0], (gunLocation))
        ##################################################

        d2.miniMapRenderer(screen, plx, ply, pla, pygame,
                           mp, gr, miniMapResolution)
        # break

        ##################################################
        #           Croshair
        ##################################################
        pygame.draw.circle(screen, (255, 255, 255), (gr[0]/2, gr[1]/2), 30, 3)

        ########################################
        # .          Heads up display
        #########################################

        # HEALTH BAR

        # MINI MAP

        # Flip the display
        pygame.display.flip()

    if(running == False):
        gameStack.pop()
