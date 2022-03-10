
### 10 MARCH 2022
####################
from pickle import NONE
import numpy as np
import items 
import game
import matplotlib.pyplot as plt
import time
#import pygame as pg2
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_DELETE,
    K_BACKSPACE,
    K_0,
    K_a
    
)
class levelEditor:
    def __init__(self,levelObj,levelRes,config,itemprop):
        #print(levelRes)
        self.level=levelObj
        self.objList={}
        self.crntInd=0
        self.levelMap=np.zeros((config['mapResolution']))
        #print(self.levelMap.shape)
        #print((levelRes[1],levelRes[0]))
        #self.levelMap[700][0]=1
        self.config=config
        self.strp=[2,2]
        self.endPos=[0,0]
        self.CurrentObject=['',0,(0,0,0)]
        self.colorIt=[(0,0,0),(255,255,255),(255,0,0),(0,255,0)]
        #keyList=[K_UP,0
        #K_DOWN,1
        #K_LEFT,2
        #K_RIGHT,3
        #K_ESCAPE,4
        #KEYDOWN,5
        #QUIT,6
        #K_SPACE,]7
        #########################################################
        # EXPLAINATORY ABOUT WORKING OF LEVEL MAP :
        # 1. Map consists of level item object ....   but to implement this .... 
        # level map .. stores index. of the object in objList.. so the whole area that an object covers
        # will consists of a no that indicated the index of that object 
        #
        # BAD EXPLAINATION But LETS HOPE IT REMIDES ME WHAT THIS FUNCTION DOES......--\/-- .. 
        #########################################################
    def drop(self,itemp):
        self.CurrentObject=itemp
    def draw(self,screen,config):
        for i in range(0,self.config['mapResolution'][0]):
            self.config['pygame'].draw.line(screen, (255, 255, 255), (i*self.config['mul']+self.config['itemListWidth'], 0), (i*self.config['mul']+self.config['itemListWidth'], self.config['mapResolution'][1]*self.config['mul']))
        for i in range(0,self.config['mapResolution'][1]):
            self.config['pygame'].draw.line(screen, (255, 255, 255), (self.config['itemListWidth'],i*self.config['mul']), ( self.config['itemListWidth']+self.config['mapResolution'][0]*self.config['mul'],i*self.config['mul']))
        for i in range(0,self.config['mapResolution'][0]):
            for y in range(0,self.config['mapResolution'][1]):
                if(self.levelMap[i][y]!=0):
                    self.config['pygame'].draw.rect(screen, self.colorIt[int(self.levelMap[i][y])], config['pygame'].Rect(i*self.config['mul']+self.config['itemListWidth'],y*self.config['mul'],self.config['mul'],self.config['mul']))
    def inputMouse(self,mouseLoc):
        loc=[(mouseLoc[0]-self.config['itemListWidth'])//self.config['mul'], mouseLoc[1]//self.config['mul']]
        if(self.CurrentObject[1]==1):
            self.strp=[loc[0]+0.5,loc[1]+0.5]
        elif(self.CurrentObject[1]==2):
            self.endPos=[loc[0]+0.5,loc[1]+0.5]
        
        self.levelMap[loc[0]][loc[1]]=self.CurrentObject[1]
    
class itemList:
    def __init__(self,screenObj,configHash={}):
        ### Object of the screen on witch level will be rendered
        self.List = [['block',1,(255,255,255)], ['startPoint',2,(255,0,0)], ['levelEnd',3,(0,255,0)]]
        self.screen=screenObj
        self.config=configHash
        self.itemElementheight=40
    def drag(self,loc):
        itno=loc[1]//self.itemElementheight
        if(itno>=5):
            return ['none']
        return self.List[itno-1]
        ##this object gets the location of the click and return the object     
    def draw(self):
        self.config['pygame'].draw.rect(self.screen, (10, 10, 10), self.config['pygame'].Rect(0, 0, self.config['itemListWidth'], self.config['GameResolution'][1]-self.config['GameResolution'][1]//2))
        txt = self.config['font'].render("ITEM LIST", True, (0, 0, 255))
        self.screen.blit(txt, (10,  10))
        for i in range(len(self.List)):
            txt = self.config['font'].render(self.List[i][0], True, (0, 0, 255))
            self.screen.blit(txt, (10, self.itemElementheight*(i+2) - self.itemElementheight/2))
            self.config['pygame'].draw.rect(self.screen, self.List[i][2], self.config['pygame'].Rect(100,self.itemElementheight*(i+2) - self.itemElementheight/2 , 10,10))
class itemProp:
    def  __init__(self,screen,config):
        self.item=None
        self.config=config
        self.screen=screen
        self.loc=[0,0]
    def setCuttentItem(self,item,loc):
        self.item=item
        self.loc=loc
    def draw(self):
        txt = self.config['font'].render('width:', True, (235, 235, 235))
        self.screen.blit(txt, (self.config['itemListWidth']+10, self.config['GameResolution'][1]-self.config['itemPropHeight']+35))
        txt = self.config['font'].render('height:', True, (235, 235, 235))
        self.screen.blit(txt, (self.config['itemListWidth']+10, self.config['GameResolution'][1]-self.config['itemPropHeight']+50))
        txt = self.config['font'].render('x:', True, (235, 235, 235))
        self.screen.blit(txt, (self.config['itemListWidth']+270, self.config['GameResolution'][1]-self.config['itemPropHeight']+35))
        txt = self.config['font'].render('y:', True, (235, 235, 235))
        self.screen.blit(txt, (self.config['itemListWidth']+270, self.config['GameResolution'][1]-self.config['itemPropHeight']+50))
        if(self.item!=None):
            # PRINT SIZE
            self.item.prop['size'][0]
            txt = self.config['font'].render(str(self.item.prop['size'][0]), True, (235, 235, 235))
            self.screen.blit(txt, (self.config['itemListWidth']+70, self.config['GameResolution'][1]-self.config['itemPropHeight']+35))
            txt = self.config['font'].render(str(self.item.prop['size'][1]), True, (235, 235, 235))
            self.screen.blit(txt, (self.config['itemListWidth']+70, self.config['GameResolution'][1]-self.config['itemPropHeight']+50))
            self.item.prop['size'][0]
            txt = self.config['font'].render(str(self.loc[0]), True, (235, 235, 235))
            self.screen.blit(txt, (self.config['itemListWidth']+340, self.config['GameResolution'][1]-self.config['itemPropHeight']+35))
            txt = self.config['font'].render(str(self.loc[1]), True, (235, 235, 235))
            self.screen.blit(txt, (self.config['itemListWidth']+340, self.config['GameResolution'][1]-self.config['itemPropHeight']+50))

            #pass
             #txt = self.config['font'].render(self.List[i], True, (0, 0, 255))
            #self.screen.blit(txt, (10, self.itemElementheight*(i+2) - self.itemElementheight/2))
class MenueItems:
    def __init__(self,screen,config,levelEditorObj):
        self.screen=screen
        self.config=config
        self.exitSatat=False
        self.levelEditor=levelEditorObj
    def Input(self,loc):
        #print(True)
        #print(loc[1]-self.config['GameResolution'][1]//2+20)
        if(loc[1]<self.config['GameResolution'][1]//2+40):
            ############################################
            # Converting Engine Level To Game LEVEL
            # Changing the index so its usable by game 
            ############################################
            lvm=self.levelEditor.levelMap #level map 
            #plt.imshow(lvm)
            #plt.show()
            glm=np.zeros((lvm.shape[1],lvm.shape[0])) #game level map
            for i in range(len(lvm)):
                for y in range(len(lvm[0])):
                    if(lvm[i][y]!=0):
                        glm[y][i]=1
            for i in glm[0]:
                i=1
            for i in glm[-1]:
                i=1
            for i in range(len(glm)):
                glm[i][0]=1
                glm[i][-1]=0
            plt.imshow(glm)
            plt.show()
            #self.strp=[2,2]
            #self.endPos=[0,0]
            self,levelEditor.self.CurrentObject=['',0,(0,0,0)]
            gobj=game.Game(glm,[self.levelEditor.strp[1],self.levelEditor.strp[0]],[self.levelEditor.endPos[1],self.levelEditor.endPos[0]])
            gobj.startGame()
        elif(loc[1]<self.config['GameResolution'][1]//2+70):
            #save game level
            running=True
            levelName=""
            preseed=0
            presstime=0
            while running:
                for event in self.config['pygame'].event.get():
                    if event.type == self.config['pygame'].QUIT:
                        running=False
                mousePos = self.config['pygame'].mouse.get_pos()
                pressed_keys = self.config['pygame'].key.get_pressed()
                self.config['pygame'].draw.rect(self.screen, (40,40,40), self.config['pygame'].Rect(0,0 , 400,200))
                txt = self.config['font'].render(('Enter Level Name :'), True, (255, 255, 255))
                self.screen.blit(txt, (10,10))
                txt = self.config['font'].render((levelName), True, (255, 255, 255))
                self.screen.blit(txt, (10,40))
                txt = self.config['font'].render(('SAVE'), True, (255, 255, 255))
                self.screen.blit(txt, (40,70))
                self.config['pygame'].display.flip()
                ###################################################
                #KEY PRESS HANDLER 
                ###################################################
                # alphabet
                if(preseed==0):
                    for i in range(97,123):
                        if(pressed_keys[i]):
                            levelName=levelName+chr(ord('a')+(i-97))
                            preseed=1
                            presstime=time.time()
                            break
                    if(pressed_keys[K_BACKSPACE]):
                        levelName=levelName[:-1]
                        preseed=1
                        presstime=time.time()
                if(time.time()-presstime>=0.1):
                    preseed=0
                ###################################################
                #CLICK EVENT HANDLER 
                ###################################################
                if(len(levelName)!=0 and self.config['pygame'].mouse.get_pressed()[0] and mousePos[0]>=40 and mousePos[1]>=70 and mousePos[0]<=80 and mousePos[1]<=100):
                    
                    running=False
                    pass

               


                
            pass
        elif(loc[1]<self.config['GameResolution'][1]//2+70):
            pass
        elif(loc[1]<self.config['GameResolution'][1]//2+95):
            self.exitSatat=True
    def draw(self):
        txt = self.config['font'].render('Run Game', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+20))
        txt = self.config['font'].render('Save', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+45))
        txt = self.config['font'].render('Load', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+70))
        txt = self.config['font'].render('Exit', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+95))
        return self.exitSatat