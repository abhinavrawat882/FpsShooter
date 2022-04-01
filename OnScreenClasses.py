### 10 MARCH 2022
####################
from pickle import NONE
from xml.dom import NotFoundErr
import numpy as np
import items 
import game
import matplotlib.pyplot as plt
import time
import os
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


##############################################################################
##
##                          MAIN MENUE
##############################################################################
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
            
            gobj=game.Game(glm,[self.levelEditor.strp[1],self.levelEditor.strp[0]],[self.levelEditor.endPos[1],self.levelEditor.endPos[0]])
            gobj.startGame()
            self.config['pygame'].display.set_mode(self.config['GameResolution'])
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
                if(time.time()-presstime>=0.15):
                    preseed=0
                ###################################################
                #CLICK EVENT HANDLER 
                ###################################################
                if(len(levelName)!=0 and self.config['pygame'].mouse.get_pressed()[0] and mousePos[0]>=40 and mousePos[1]>=70 and mousePos[0]<=80 and mousePos[1]<=100):
                    crdl=os.listdir()
                    if( "levels" not in crdl):
                        os.mkdir("levels")
                    LevelFile=open("levels/"+levelName+".lvl",'w')
                    ### first write levels
                    mpd=""
                    for i in self.levelEditor.levelMap:
                        for y in i:
                            mpd+=str(int(y))+","
                        mpd=mpd[:-1]+' '
                    print(mpd)
                    LevelFile.write(mpd)
                    LevelFile.write(str(self.levelEditor.strp[0])+" "+str(self.levelEditor.strp[1])) 
                    LevelFile.write(" "+str(self.levelEditor.endPos[0])+" "+str(self.levelEditor.endPos[1]))
                    LevelFile.close()
                    #self.strp=[2,2]
                    #self.endPos=[0,0]
                    running=False
        elif(loc[1]<self.config['GameResolution'][1]//2+95):
            #############################################################
            # LOAD SCREEN
            #############################################################
            running=True
            levelName=""
            preseed=0
            presstime=0
            dirlst=os.listdir('levels')
            self.config['pygame'].display.set_mode((1200,700))
            dx=1200//5
            dy=700//3
            ofset=30
            while running:
                mousePos = self.config['pygame'].mouse.get_pos()
                for event in self.config['pygame'].event.get():
                    if event.type == self.config['pygame'].QUIT:
                        running=False
                for i in range(len(dirlst)):
                    self.config['pygame'].draw.rect(self.screen, (60,60,60), self.config['pygame'].Rect(ofset+10+dx*(i%5),ofset+10+dy*(i//5),dx-10-ofset,dy-10-ofset))
                    txt = self.config['font'].render(dirlst[i], True, (235, 235, 235))
                    self.screen.blit(txt, (ofset+20+dx*(i%5),ofset+20+dy*(i//5)))
                if(self.config['pygame'].mouse.get_pressed()[0]):
                    x=mousePos[0]//dx
                    y=mousePos[1]//dy
                    ind=y*5 + x
                    #print(ind)
                    try:
                        levelName=dirlst[ind]
                    except:
                        continue
                    LevelFile=open("levels/"+levelName,'r')
                    levelStr=LevelFile.read().split()#[1:-1]
                    LevelFile.close()
                    print(levelStr)
                    posloc=levelStr[-4:]
                    print(posloc)
                    levelStr=levelStr[:-4]
                    #print(levelStr)
                    level=[]
                    for i in levelStr:
                        level.append(list(map(int,i.split(','))))
                    #plt.imshow(level)
                    #plt.show()
                    #print("YESS")
                    self.levelEditor.levelMap=np.array(level)
                    self.levelEditor.strp=[float(posloc[0]),float(posloc[1])]
                    self.levelEditor.endPos=[float(posloc[2]),float(posloc[3])]
                    #self.strp=[2,2]
                    #self.endPos=[0,0]
                    running=False
                    #except:
                        #print("err")
                    #    pass
                self.config['pygame'].display.flip()
            self.config['pygame'].display.set_mode((self.config['GameResolution']))
        elif(loc[1]<self.config['GameResolution'][1]//2+115):
            #############################################################
            #          LEVEL PROGRESSION CONFIGURATOR
            #############################################################
            running=True
            levelName=""
            preseed=0
            presstime=0
            dirlst=os.listdir('levels')
            #######################################################
            #importing Game Level Progression File
            #######################################################
            levelFile=None
            connections=[]

            ##############################
            # SAVE CoNFIG FILE Architecture
            #
            #  "LevelName" : "Name of level With outgoing connection"
            #
            #
            ###############################
            
            self.config['pygame'].display.set_mode((1200,700))
            dx=1200//5
            dy=700//3
            ofset=30
            isDragged=False
            draggedPoint=[]
            cind=-1
            ###########################################################
            # IMPORTING LEVEL NAME AND REFERENCES
            ###########################################################
            dict={} #level id  => level NAME
            dicts={} # LEVEL NAME => LEVEL ID
            
            for i in range(len(dirlst)):
                dict[i]=dirlst[i]
                dicts[dirlst[i]]=i
                connections.append(-1)
            ###########################################################  





            ###########################################################
            # IMPORTING CONNECTIONS
            ###########################################################
            #try:
            levelFile=open("levelProgression.lvl",'r')
            levelLines=list(levelFile.read().split('-'))
            print(levelLines)
            
            for i in levelLines:
                if(i==''):
                    break
                levelFrom,levelTo=i.split()
                connections[dicts[levelFrom]]=dicts[levelTo]
            levelFile.close()
            #except:
            #    levelFile=open("levelProgression.lvl",'w')
            #    levelFile.close()
            ###########################################################



            print(connections)
            #############################################################
            #                   BLUEPRINT LOOP
            #############################################################
            while running:
                self.screen.fill((0,0,0))
                mousePos = self.config['pygame'].mouse.get_pos()
                for event in self.config['pygame'].event.get():
                    if event.type == self.config['pygame'].QUIT:
                        levelFile=open("levelProgression.lvl",'w')
                        for i in range(len(connections)):
                            if connections[i]!=-1:
                                levelFile.write(dict[i]+" "+dict[connections[i]]+"-")
                        levelFile.close()
                        running=False
                for i in range(len(dirlst)):
                    self.config['pygame'].draw.rect(self.screen, (60,60,60), self.config['pygame'].Rect(ofset+10+dx*(i%5),ofset+10+dy*(i//5),dx-10-ofset,dy-10-ofset))
                    txt = self.config['font'].render(dirlst[i], True, (235, 235, 235))
                    self.screen.blit(txt, (ofset+20+dx*(i%5),ofset+20+dy*(i//5)))
                    #Start
                    self.config['pygame'].draw.rect(self.screen, (0,255,0), self.config['pygame'].Rect(ofset+10+dx*(i%5),dy*((i//5)+1)-ofset-10,10,10))
                    #END
                    self.config['pygame'].draw.rect(self.screen, (0,0,255), self.config['pygame'].Rect(dx*((i%5)+1)-ofset-10,dy*((i//5)+1)-ofset-10,10,10))
                
                for i in range(len(connections)):
                    if connections[i]!=-1:
                        # SENDING :
                        #[ dx*((i%5)+1)-ofset-5,dy*((i//5)+1)-ofset-5]
                        # ACCEPTING :
                        #[ofset+10+dx*(i%5)+5,dy*((i//5)+1)-ofset-5]
                        #print("here")
                        self.config['pygame'].draw.line(self.screen, (200,250,200), ( dx*((i%5)+1)-ofset-5,dy*((i//5)+1)-ofset-5), (ofset+10+dx*(connections[i]%5)+5,dy*((connections[i]//5)+1)-ofset-5),2)
                        self.config['pygame'].draw.rect(self.screen, (255,0,0), self.config['pygame'].Rect(ofset+10+dx*(connections[i]%5)+5,dy*((connections[i]//5)+1)-ofset-5,10,20))
                ########################################################################
                # CLICK EVENT HANDLER
                #########################################################################
                x=mousePos[0]//dx
                y=mousePos[1]//dy
                i=y*5 + x
                #####################################################################
                #               Dragging to connect end to start point
                ######################################################################
                if(self.config['pygame'].mouse.get_pressed()[0] and isDragged==False):
                    #dx*((i%5)+1)-ofset-10,dy*((i//5)+1)-ofset-10,10,10)
                    if(mousePos[0] > dx*((i%5)+1)-ofset-10 and mousePos[0] < dx*((i%5)+1)-ofset and  mousePos[1] > dy*((i//5)+1)-ofset-10 and mousePos[1] < dy*((i//5)+1)-ofset):
                        isDragged=True
                        cind=i
                        print(cind)
                        draggedPoint=[ dx*((i%5)+1)-ofset-5,dy*((i//5)+1)-ofset-5]
                        self.config['pygame'].draw.rect(self.screen, (0,255,0), self.config['pygame'].Rect(mousePos[0],mousePos[1],10,10))
                #############################################################################\
                #           IF A  END POINT IS CURRRENTLY BEING DRAGGED OR NOT
                ##############################################################################
                elif(self.config['pygame'].mouse.get_pressed()[0] and isDragged):
                    try:
                        self.config['pygame'].draw.line(self.screen, (200,250,200), draggedPoint, mousePos,2)
                        self.config['pygame'].draw.rect(self.screen, (255,0,0), self.config['pygame'].Rect(mousePos[0],mousePos[1],10,20))
                    except:
                        pass
                #################################################################################
                #                   DROPPING END POINT 
                #################################################################################
                elif( not self.config['pygame'].mouse.get_pressed()[0] and isDragged):
                    if(mousePos[0] > ofset+10+dx*(i%5) and mousePos[0] < ofset+10+dx*(i%5)+10 and  mousePos[1] > dy*((i//5)+1)-ofset-10 and mousePos[1] < dy*((i//5)+1)-ofset):
                        connections[cind]=i
                        print(cind,i)
                ########################################################################
                #                   DRAGGING IS STOPED
                ########################################################################
                if self.config['pygame'].mouse.get_pressed()[0]==False:
                    isDragged=False
                    draggedPoint=[] 
                self.config['pygame'].display.flip() 
            ############################################################################################


            self.config['pygame'].display.set_mode((self. config['GameResolution']))
        
        elif loc[1]<self.config['GameResolution'][1]//2+130:
            ####################################################################################
            #           GAME COMPILER
            ####################################################################################
            
            self.exitSatat=True 
    def draw(self):
        txt = self.config['font'].render('Run Game', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+20))
        txt = self.config['font'].render('Save', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+45))
        txt = self.config['font'].render('Load', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+70))
        txt = self.config['font'].render('Level CMP', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+95))
        txt = self.config['font'].render('Compile', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+115))
        txt = self.config['font'].render('Exit', True, (235, 235, 235))
        self.screen.blit(txt, (10, self.config['GameResolution'][1]/2+130))
        return self.exitSatat