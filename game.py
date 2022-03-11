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

import math
import GameEnigneLib.AngleCal as ac
import GameEnigneLib.D2Engine as d2
import GameEnigneLib.D3renderer as d3
import GameEnigneLib.lineTracer as lt
import GameEnigneLib.preCalculations as pc
import copy



class Game:
    def __init__(self,level,strpos,endpos):
        self.playerSpeed=0.04
        self.running = True
        self.FOV = 45
        self.gr = (1280, 720)
        self.playerSpeed = 0.1
        self.angularStep=4
        self.plx = strpos[0]  # player position in x
        self.ply = strpos[1]  # player position in y
        self.pla = 0 # player view angle
        self.ang = 0
        #      PERSON GUN IMAGES
        self.gnimg0 = pygame.image.load(
            r"Assets/Gun/gun.png")
        self.gnimg1 = pygame.image.load(
            r"Assets/Gun/gun1.png")
        self.gnimg2 = pygame.image.load(
            r"Assets/Gun/gun2.png")
        self.gnimg3 = pygame.image.load(
            r"Assets/Gun/gun3.png")
        self.gnimg = []
        self.gnimg.append(self.gnimg0)
        self.gnimg.append(self.gnimg1)
        self.gnimg.append(self.gnimg2)
        self.gnimg.append(self.gnimg3)
        # GUN IMAGE ON SCREEN
        self.gt = 0
        ## ENEMY IMAGES####
        self.enemyWalking = pygame.image.load(r"Assets/Enemy/enemyW.png")
        self.enemyShooting = pygame.image.load(r"Assets/Gun/gun1.png")
        self.enemyWalking = pygame.transform.scale(self.enemyWalking, (400,720))
        self.ewr=(400,720)
        ############################
        # PRECALCULATE VARIABLES
        self.gunLocation = (self.gr[0]/2+30, self.gr[1]-230)
        self.cs, self.si, self.noa, self.angleBeetweenLines, self.lineAngle, self.dy, self.dx, self.llpy, self.llpx,self.d3angularStep = pc.calc(
            self.FOV, self.pla, self.angularStep, self.gr)
        self.MapSize = [level.shape[0],level.shape[1]]
        self.miniMapResolution = (48, 48)
        self.mp = level
        #  enemyList Template
        #  [TypeOfEnemy ,x,y,health,time of death]
        self.enemyList=[[1,2,2,50,-1]]
        # This is a list of enemy's each element in the list is enemy template giving info about the enemy
        self.gtimer = 0
    ######################
    # INPUT EVENT HANDLER
    ######################
    def update(self,pressed_keys, x, y, a, ang, cs, si, noa, angStep, gtimer, gt):
        run = True
        if pressed_keys[K_UP]:

            x += self.playerSpeed*cs[ang]
            y += self.playerSpeed*si[ang]
        if pressed_keys[K_DOWN]:
            x -= self.playerSpeed*cs[ang]
            y -= self.playerSpeed*si[ang]
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
    def startGame(self):
        pygame.init()
        screen = pygame.display.set_mode(self.gr)
        ########################################
        # .          GAME LOOP
        #########################################
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            ########################################
            # .          CLICK EVENT HANDLER
            #########################################
            pressed_keys = pygame.key.get_pressed()
            # print(pressed_keys)
            self.plx, self.ply, self.pla, self.running, self.ang, self.gtimer, self.gt = self.update(
                pressed_keys, self.plx, self.ply, self.pla, self.ang, self.cs, self.si, self.noa, self.angularStep, self.gtimer, self.gt)

            ########################################
            # .          DRAW ON SCREEN
            #########################################
            # the background with white
            screen.fill((0, 0, 0))

            ##Draw the main seen
            d3.threDRenderer(self.plx, self.ply, screen,pygame,self.gr,self.lineAngle,self.angleBeetweenLines,self.ang,self.dy,self.dx,self.llpy,self.llpx,self.mp)

            ################################
            ##Now On TOP OF SEEN DRAW ENEMY
            ################################
            #
            #for enemy in self.enemyList:
            #    #  enemyList Template
            #    #  [0: TypeOfEnemy ,1: x,2: y,3 : health,4 :time of death]
            #    y=self.ply-enemy[2]
            #    x=self.plx-enemy[1]
            #    Ene_ply_ang=math.tanh(abs(y)/abs(x))
            #
            #    la=ac.giveAbsAngle(Ene_ply_ang*180/math.pi)
            #    if(y<0 and x<0):
            #        la=180+la
            #    elif(y<0 and x>=0):
            #        la=360-la
            #    elif(y>=0 and x<0):
            #        la=180-la
            #    ea=ac.giveAbsAngle(self.pla-self.FOV)
            #    sa=ac.giveAbsAngle(self.pla+self.FOV)
            #    doIt=0
            #    if(sa>=0 and ea<360 and sa <90 and ea>270):
            #        if la<sa or la>ea:
            #            doIt=1
            #    else:
            #        if la<sa and la>ea:
            #            doIt=1
            #
            #    if(doIt==1):
            #        dist_ene_player=((self.plx-enemy[1])**2 + (self.ply-enemy[2])**2)**(0.5)
            #        edy=(math.sin(la*math.pi/180))
            #        edx=(math.cos(la*math.pi/180))
            #        ellpy=(abs( 1/math.sin(la*math.pi/180)))
            #        ellpx=(abs(1/math.cos(la*math.pi/180)))
            #        ln,inter,xe,ye=lt.lineTracer(self.plx, self.ply,la, self.mp, edy,edx,ellpy,ellpx)
            #        ss=abs(sa-la)
            #        es=abs(ea-la)
            #        sc=0
            #
            #        ewrc=[self.ewr[0],self.ewr[1]]
            #        ewrc[0]/=ln
            #        ewrc[1]/=ln
            #        enemyWalkingc = pygame.transform.scale(self.enemyWalking,ewrc )
            #        if(ss<es):
            #            sc=ss*(1/self.d3angularStep)-self.ewr[0]/2
            #        else:
            #            sc=self.gr[0]-es*(1/self.d3angularStep)-ewrc[0]/2
            #        screen.blit(enemyWalkingc,(sc,(self.gr[1]/2)-(ewrc[1]/2)))
            #NEXT LAYER IS GUN 
            if(self.gtimer==1):
                if(time.time()-self.gt>0.9):
                    gtimer=0
                    screen.blit(self.gnimg[0],(self.gunLocation))

                elif(time.time()-self.gt>0.6):
                    screen.blit(self.gnimg[3],(self.gunLocation))
                elif(time.time()-self.gt>0.3):
                    screen.blit(self.gnimg[2],(self.gunLocation))
                else:    
                    screen.blit(self.gnimg[1],(self.gunLocation))
            else:
                screen.blit(self.gnimg[0], (self.gunLocation))
            ##################################################

            #d2.miniMapRenderer(screen, self.plx, self.ply, self.pla, pygame,
            #                   self.mp, self.gr, self.miniMapResolution)
            # break

            ##################################################
            #           Croshair
            ##################################################
            pygame.draw.circle(screen, (255, 255, 255), (self.gr[0]/2, self.gr[1]/2), 30, 3)

            ########################################
            # .          Heads up display
            #########################################

            # HEALTH BAR

            # MINI MAP

            # Flip the display
            pygame.display.flip()
