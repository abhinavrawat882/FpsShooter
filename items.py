class block:
    def __init__(self):
        self.prop={'size':[20,20]}
        self.name='block'
        #$self.pos=0
    def draw(self,screen,config,loc):
        config['pygame'].draw.rect(screen, (255, 255, 255), config['pygame'].Rect(loc[0],loc[1],int(self.prop['size'][0]),int(self.prop['size'][1])))
    def level(self,levelMap,pos,ind):
        for x in range(pos[0],pos[0]+int(self.prop['size'][0])+1):
            for y in range(pos[1],pos[1]+int(self.prop['size'][1])+1):
                levelMap[x][y]=ind
    def remove(self,levelMap,pos):
        for x in range(pos[0],pos[0]+int(self.prop['size'][0])+1):
            for y in range(pos[1],pos[1]+int(self.prop['size'][1])+1):
                levelMap[x][y]=0
class circle:
    def __init__(self):
        self.prop={'size':[20,20]}
        self.prop=[]
        self.name='circle'
    def draw(self,screen,config,mouseloc):
        pass
    def level(self,levelMap,pos):
        pass
class startPoint:
    def __init__(self):
        self.prop={'size':[20,20]}
        self.prop=[]
        self.name='startPoint'
    def draw(self,screen,config,mouseloc):
        pass
    def level(self,levelMap,pos):
        pass
class levelEnd:
    def __init__(self):
        self.prop={'size':[20,20]}
        self.prop=[]
        self.name='LevelEnd'
    def draw(self,screen,config,mouseloc):
        pass
    def level(self,levelMap,pos):
        pass
