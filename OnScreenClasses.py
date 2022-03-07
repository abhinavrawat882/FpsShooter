
from pickle import NONE
import numpy as np
import items 
import game
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
)
class levelEditor:
    def __init__(self,levelObj,levelRes,config,itemprop):
        #print(levelRes)
        self.level=levelObj
        self.objList={}
        self.crntInd=0
        self.levelMap=np.zeros((levelRes))
        #print(self.levelMap.shape)
        #print((levelRes[1],levelRes[0]))
        #self.levelMap[700][0]=1
        self.config=config
        self.CurrentObject=None
        self.CurrentIndex=0
        self.itemProp=itemprop
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
    def drop(self,itemobj,loc):
        self.crntInd+=1
        self.objList[self.crntInd]=[itemobj,[loc[0],loc[1]]]
        
        self.CurrentObject=self.objList[self.crntInd][0]
        self.CurrentIndex=self.crntInd
        self.itemProp.setCuttentItem(itemobj,loc)
        #print(loc[0]-self.config['itemListWidth'],loc[1]-self.config['itemPropHeight'])
        self.objList[self.crntInd][0].level(self.levelMap,(loc[0]-self.config['itemListWidth'],loc[1]),self.crntInd)
    def draw(self,screen,config):
        txt = self.config['font'].render(str(self.CurrentIndex), True, (0, 0, 255))
        screen.blit(txt, (self.config['itemListWidth']+ 10 ,  10))
        for i in range(1,self.crntInd+1):
            if(i in self.objList):
                self.objList[i][0].draw(screen,config,self.objList[i][1])
    def inputMouse(self,mouseLoc,pmop,isCurrentObjectDragged):
        ind=int(self.levelMap[mouseLoc[0]-self.config['itemListWidth']][mouseLoc[1]])
        if(isCurrentObjectDragged==False):
            if ind==0:
                self.CurrentObject=None
                self.CurrentIndex=0
                return
            self.CurrentObject=self.objList[ind][0]
            self.CurrentIndex=ind
            self.itemProp.setCuttentItem(self.CurrentObject,self.objList[self.CurrentIndex][1])
        else:
            if(self.CurrentObject==None):
                return
            self.CurrentObject.remove(self.levelMap,(self.objList[self.CurrentIndex][1][0]-self.config['itemListWidth'],self.objList[self.CurrentIndex][1][1]))
            self.objList[self.CurrentIndex][1][0]+=mouseLoc[0]-pmop[0]
            self.objList[self.CurrentIndex][1][1]+=mouseLoc[1]-pmop[1]
            self.CurrentObject.level(self.levelMap,[self.objList[self.CurrentIndex][1][0]-self.config['itemListWidth'],self.objList[self.CurrentIndex][1][1]],self.CurrentIndex)

        


    def inputKeyBoard(self,keyPressed):
        #print('here')
        #print(self.keyList[0])
        if(self.CurrentObject==None):
            #print('hello')
            return
        #print(keyPressed[self.keyList[0]])
        #print(True in keyPressed)
        if keyPressed[K_UP]  : #self.CurrentObject.prop['size'][1]+0.2<=40:
            self.CurrentObject.prop['size'][1]+=0.2
            
            #print("key pressed up")
        elif keyPressed[K_DOWN] and self.CurrentObject.prop['size'][1]-0.2>=14:
            self.CurrentObject.prop['size'][1]-=0.2
            #print("key pressed d")
        elif keyPressed[K_LEFT] and self.CurrentObject.prop['size'][0]-0.2>=14:
            self.CurrentObject.prop['size'][0]-=0.2
            #print("key pressed l")
        elif keyPressed[K_RIGHT]:# and self.CurrentObject.prop['size'][0]+0.2<=40:
            self.CurrentObject.prop['size'][0]+=0.2
            #print("key pressed r")
        elif keyPressed[K_BACKSPACE]:
            #print("delete karo")
            if(self.CurrentObject!=None):
                del self.objList[self.CurrentIndex]
                self.CurrentObject=None
                self.CurrentIndex=0
                return
        self.CurrentObject.level(self.levelMap,(self.objList[self.CurrentIndex][1][0]-self.config['itemListWidth'],self.objList[self.CurrentIndex][1][1]),self.CurrentIndex)
class itemList:
    def __init__(self,screenObj,configHash={}):
        ### Object of the screen on witch level will be rendered
        self.ListCls = [items.block,items.circle, items.startPoint, items.levelEnd]
        self.List = ['block','circle', 'startPoint', 'levelEnd']
        self.screen=screenObj
        self.config=configHash
        self.itemElementheight=40
    def drag(self,loc):
        #print("clicked")
        itno=loc[1]//self.itemElementheight
        if(itno>=5):
            return None
        return self.ListCls[itno-1]()
        ##this object gets the location of the click and return the object     
    def draw(self):
        self.config['pygame'].draw.rect(self.screen, (10, 10, 10), self.config['pygame'].Rect(0, 0, self.config['itemListWidth'], self.config['GameResolution'][1]-self.config['GameResolution'][1]//2))
        txt = self.config['font'].render("ITEM LIST", True, (0, 0, 255))
        self.screen.blit(txt, (10,  10))
        for i in range(len(self.List)):
            txt = self.config['font'].render(self.List[i], True, (0, 0, 255))
            self.screen.blit(txt, (10, self.itemElementheight*(i+2) - self.itemElementheight/2))
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
        if(loc[1]>self.config['GameResolution'][1]//2+20):
            ############################################
            # Converting Engine Level To Game LEVEL
            # Changing the index so its usable by game 
            ############################################
            lvm=self.levelEditor.levelMap #level map 
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
            ###############################################
            #REDUCE GAME MAP RESOLUTION 
            # by 4 times
            ################################################
            rr=8
            rglm=np.zeros((int(glm.shape[1]//rr),int(glm.shape[0]//rr))) #reduced game level map
            rglmi=0
            
            for i in range(0,len(glm),rr):
                rglmy=0
                for y in range(0,len(glm[0]),rr):
                    mx=0
                    for xi in range(i,i+rr):
                        for yi in range(y,y+rr):
                            try:
                                mx=max(glm[xi][yi],mx)
                            except:
                                mx=1
                                break
                    rglm[rglmi][rglmy]=mx
            gobj=game.Game(rglm)
            gobj.startGame()
        elif(loc[1]<self.config['GameResolution'][1]//2+45):
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