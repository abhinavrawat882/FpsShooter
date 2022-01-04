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
import GameEnigneLib.preCalculations as pc
gr=(1280,720)
playerSpeed=0.08
import time



######################
#INPUT EVENT HANDLER
######################
def update(pressed_keys, x, y, a,ang,cs,si,noa,angStep,gtimer,gt):
    run=True
    if pressed_keys[K_UP]:

        x += playerSpeed*cs[ang]
        y += playerSpeed*si[ang]
    elif pressed_keys[K_DOWN]:
        x -= playerSpeed*cs[ang]
        y -= playerSpeed*si[ang]
    elif pressed_keys[K_LEFT]:
        a += angStep
        ang+=1
    elif pressed_keys[K_RIGHT]:
        a -= angStep
        ang-=1
    elif pressed_keys[K_SPACE] and gtimer==0:
        gt=time.time()
        gtimer=1
    
    
    
    if(ang>noa):
        ang=0
    elif(ang<0):
        ang=noa

    elif pressed_keys[K_ESCAPE]:
        run=False
    a = ac.giveAbsAngle(a)
    # print(a)
    return(x, y, a,run,ang,gtimer,gt)


def startGame(pygame,screen,gameStack,settings):
    #############################################################
    #                   LOAD GAME
    #############################################################
    

    angularStep=2
    plx = 12  # player position in x
    ply = 7  # player position in y
    pla = 0  # player view angle
    ang=0

    ## FIRST PERSON GUN IMAGES
    gnimg0=pygame.image.load(r"C:\Users\abhin\Documents\Projects\FpsShooter\Assets\Gun\gun.png")
    gnimg1=pygame.image.load(r"C:\Users\abhin\Documents\Projects\FpsShooter\Assets\Gun\gun1.png")
    gnimg2=pygame.image.load(r"C:\Users\abhin\Documents\Projects\FpsShooter\Assets\Gun\gun2.png")
    gnimg3=pygame.image.load(r"C:\Users\abhin\Documents\Projects\FpsShooter\Assets\Gun\gun3.png")
    gnimg=[]
    gnimg.append(pygame.transform.scale(gnimg0,( 260,230)))
    gnimg.append(pygame.transform.scale(gnimg1,( 260,230)))
    gnimg.append(pygame.transform.scale(gnimg2,( 260,230)))
    gnimg.append(pygame.transform.scale(gnimg3,( 260,230)))
    
    #GUN IMAGE ON SCREEN

    gt=0
    ## PRECALCULATE VARIABLES
    gunLocation=(gr[0]/2+30,gr[1]-230)
    cs,si,noa,angleBeetweenLines,lineAngle,dy,dx,llpy,llpx= pc.calc(FOV,pla,angularStep,gr)
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

    gtimer=0
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
        plx, ply, pla,running,ang,gtimer,gt = update(pressed_keys, plx, ply, pla,ang,cs,si,noa,angularStep,gtimer,gt)
        
        
        
        ########################################
        # .          DRAW ON SCREEN
        #########################################
        #print("ANGLE :",pla)
        # the background with white
        screen.fill((0, 0, 0))
        #ln,inter,xe,ye = rf.lineTracer(plx, ply, pla, mp)
        #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(gr[0]-miniMapResolution[0]-12,gr[1]-miniMapResolution[1]-10,miniMapResolution[0]+10,miniMapResolution[1]+10 ))
        #print(gr[0]-miniMapResolution[0]-12)
        d3.threDRenderer(plx, ply, screen,pygame,gr,lineAngle,angleBeetweenLines,ang,dy,dx,llpy,llpx,mp)
        if(gtimer==1):
            if(time.time()-gt>1.5):
                gtimer=0
                screen.blit(gnimg[0],(gunLocation))
                
            elif(time.time()-gt>1):
                screen.blit(gnimg[3],(gunLocation))
            elif(time.time()-gt>0.5):
                screen.blit(gnimg[2],(gunLocation))
            else:    
                screen.blit(gnimg[1],(gunLocation))
        else:
            screen.blit(gnimg[0],(gunLocation))
        d2.miniMapRenderer(screen, plx, ply, pla, pygame, mp,gr,miniMapResolution)
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
