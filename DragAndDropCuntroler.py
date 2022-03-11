import time
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
    def dnds(self, mouseLoc, mouseClickStatus):  # Dnds= drag and drop status
        #########################################################################
        # FUNCTION EXPLAINATION FOR FUTURE USE AND UNDERSTANDING :
        # IF Mouse is over item list and dragging something.... its in drag mode ... (running ite list code)
        # BUT if the click is over level editor .. it goes to pass through mode
        #
        #########################################################################
        unblock=True
        blockTime=0
        if(mouseClickStatus and unblock):
            if (mouseLoc[0] > self.itemListCor[0] and mouseLoc[1] > self.itemListCor[1] and mouseLoc[0] < self.itemListCor[2] and mouseLoc[1] < self.itemListCor[3]//2):
                obj = self.itemList.drag(mouseLoc)
                if(obj[0] != 'none'):
                    self.levelEditor.drop(obj)
            elif(mouseLoc[0] > self.levelEditorCor[0] and mouseLoc[1] > self.levelEditorCor[1] and mouseLoc[0] < self.levelEditorCor[2] and mouseLoc[1] < self.levelEditorCor[3]):
                self.levelEditor.inputMouse(mouseLoc)
                self.rv="levelEditor"
            elif(mouseLoc[0] >0 and mouseLoc[1] > self.config["GameResolution"][1]//2 and mouseLoc[0] < self.config['itemListWidth'] and mouseLoc[1] < self.config['GameResolution'][1]):
                #print('True')
                self.menue.Input(mouseLoc)
                unblock=False
                blockTime=time.time()
        if(not unblock and time.time()-blockTime>=4):
            unblock=True
        return self.rv