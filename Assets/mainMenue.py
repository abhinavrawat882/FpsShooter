from pygame.locals import K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,K_RETURN
import time



########################################
#    INPUT HANDLER
########################################
def updateMenue(pressed_keys, selectorLocation,keyPressStat):
    enter=False
    run=True

    if (keyPressStat[0]==0 ):
        if pressed_keys[K_UP] :
            selectorLocation-=1
            keyPressStat[0]=1
            keyPressStat[1]=time.time()

        elif pressed_keys[K_DOWN] :
            selectorLocation+=1
            keyPressStat[0]=1
            keyPressStat[1]=time.time()

        elif pressed_keys[K_RETURN] :
            enter=True

        elif pressed_keys[K_ESCAPE]:
            run=False
    else:
        if(time.time()-keyPressStat[1]>0.3 ):
            keyPressStat[0]=0

    if(selectorLocation<0):
        selectorLocation=3
    elif(selectorLocation>3):
        selectorLocation=0
    return(selectorLocation,enter,run)






########################################
# .          EXECUTE MAIN MENUE
#########################################    
def startMainMenue(pygame,gameScreen,gameStack):
    keyPressStat=[0,0]
    selectorLocation=0
    enterPress=False
    ########################################
    # .          Main Menue LOOP
    #########################################
    running = True
    while running:
        gameScreen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ########################################
        # .          CLICK EVENT HANDLER
        #########################################
        pressed_keys = pygame.key.get_pressed()
        # print(pressed_keys)
        selectorLocation,enterPress,running = updateMenue(pressed_keys, selectorLocation,keyPressStat)
        #### NOW MAKE DESSISION BASED ON User Input
        
        if(enterPress==True):
            if(selectorLocation==0):
                gameStack.append('game')
                print(gameStack)
                return()
            elif(selectorLocation==3):
                running=False

        font = pygame.font.SysFont(None, 24)
        sng = font.render('Start New Game', True, (0,0,255))
        lg = font.render('Load Game', True, (0,0,255))
        set = font.render('Setting', True, (0,0,255))
        exi = font.render('Exit', True, (0,0,255))



        ########################################
        # .          DRAW Menue
        #########################################
        selectorRectYLoc=(selectorLocation+1)*100-10
        pygame.draw.rect(gameScreen, (255, 255, 255), pygame.Rect(10,selectorRectYLoc,170,35 ))
        gameScreen.blit(sng, (20, 100))
        gameScreen.blit(lg, (20, 200))
        gameScreen.blit(set, (20, 300))
        gameScreen.blit(exi, (20, 400))
        pygame.display.flip()
    if(running==False):
        gameStack.pop()