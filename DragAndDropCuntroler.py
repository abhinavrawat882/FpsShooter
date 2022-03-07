class cuntroler:
    def __init__(self, screen, config, itemList,levelEditor,menue):
        self.config = config
        self.levelEditorCor = [self.config['itemListWidth'], 0, self.config['GameResolution'][0],
                               self.config['GameResolution'][1]- self.config['itemPropHeight']]
        self.itemListCor = [
            0, 0, self.config['itemListWidth'], self.config['GameResolution'][1]]
        self.itemPropcor = [self.config['itemListWidth'], self.config['GameResolution'][1], self.config['GameResolution']
                            [0], self.config['GameResolution'][1]-self.config['GameResolution'][0], self.config['itemPropHeight']]
        self.screen = screen
        self.objectStored = None
        self.isObjectDragged = False
        self.itemList = itemList
        self.levelEditor=levelEditor
        self.isLevelObjectDragged=False
        self.menue=menue
        self.rv='null'
    def dnds(self, mouseLoc, mouseClickStatus,pmpos):  # Dnds= drag and drop status
        #########################################################################
        # FUNCTION EXPLAINATION FOR FUTURE USE AND UNDERSTANDING :
        # IF Mouse is over item list and dragging something.... its in drag mode ... (running ite list code)
        # BUT if the click is over level editor .. it goes to pass through mode
        #
        #########################################################################
        isLevlEditorClicked=True
        
        if(mouseClickStatus == True and self.isObjectDragged == False):
            if (mouseLoc[0] > self.itemListCor[0] and mouseLoc[1] > self.itemListCor[1] and mouseLoc[0] < self.itemListCor[2] and mouseLoc[1] < self.itemListCor[3]//2):
                obj = self.itemList.drag(mouseLoc)
                if(obj != None):
                    self.isObjectDragged = True
                    self.objectStored = obj
                    self.config['pygame'].mouse.set_visible(False)
                    self.rv="itemList"
            elif(mouseLoc[0] > self.levelEditorCor[0] and mouseLoc[1] > self.levelEditorCor[1] and mouseLoc[0] < self.levelEditorCor[2] and mouseLoc[1] < self.levelEditorCor[3]):
                self.levelEditor.inputMouse(mouseLoc,pmpos,self.isLevelObjectDragged)
                self.isLevelObjectDragged=True
                self.config['pygame'].mouse.set_visible(False)
                self.rv="levelEditor"
                isLevlEditorClicked=False
            elif(mouseLoc[0] >0 and mouseLoc[1] > self.config["GameResolution"][1]//2 and mouseLoc[0] < self.config['itemListWidth'] and mouseLoc[1] < self.config['GameResolution'][1]):
                print('True')
                self.menue.Input(mouseLoc)
        if(mouseClickStatus == True and self.isObjectDragged == True):
            self.objectStored.draw(
                self.screen, self.config, mouseLoc)
        if(mouseClickStatus == False and self.isObjectDragged == True):
            if(mouseLoc[0] > self.levelEditorCor[0] and mouseLoc[1] > self.levelEditorCor[1] and mouseLoc[0] < self.levelEditorCor[2] and mouseLoc[1] < self.levelEditorCor[3]):
                #print('true')
                self.levelEditor.drop(self.objectStored,mouseLoc)
                self.rv="levelEditor"
            self.isObjectDragged = False
            self.objectStored = None
            self.config['pygame'].mouse.set_visible(True)
            
        if(isLevlEditorClicked):
            self.isLevelObjectDragged=False
            self.config['pygame'].mouse.set_visible(True)
        return self.rv