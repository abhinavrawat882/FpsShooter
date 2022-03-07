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
class kph:
    def __init__(self,levelEditor,itemList):
        self.levelEditor=levelEditor
        self.currentlySelectedOnScreenObject=None
    def pressHandler(self,screenObjectPressed,pressedKeys):
        if(screenObjectPressed=='levelEditor'):
            self.levelEditor.inputKeyBoard(pressedKeys)

