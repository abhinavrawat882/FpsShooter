import GameEnigneLib.AngleCal as ac
import GameEnigneLib.lineTracer as lt
import math
rd = 0.0174533
def threDRenderer(x, y, a, surface, mp, pygame,gr,FOV):
    lineTracer=lt.lineTracer
    # Define Variable :-
    gh = gr[1]
    gw = gr[0]
    wallHeightMul=1
    
    EndAngle = ac.giveAbsAngle(a+FOV)
    naea=a+FOV
    AngularStep = (FOV*2)/gw
    PlayerHeight = 0
    center = (gh/2)-1

    ############################################
    #             FRAME DRAWING
    ###########################################

    for i in range(0, gw):

        ###########################################
        # .    Get line length
        ###########################################
        
        la = EndAngle
        la = ac.giveAbsAngle(la)
        #print("Line Angle :",la)
        ln,inter,xe,ye = lineTracer(x, y, la, mp)

        ###########################################
        # .    Get perpendicular length
        ###########################################
        angleBeetweenLines = 0
        if(naea>a):
            angleBeetweenLines=naea-a
        elif(naea<a):
            angleBeetweenLines=a-naea

        #print("Angle Beetween  :",angleBeetweenLines)
        ln = ln*math.cos(angleBeetweenLines*rd)
        

        ###########################################
        # height calculation
        ###########################################
        try:
            height = gh/(ln)
        except:
            height=gh
        # print(height)
        height*=wallHeightMul
        ###########################################
        # Draw Column
        ###########################################
        sy = 0
        ey = 0
        if(height >= gh):
            sy = 0
            ey = gh-1

        else:
            sy = center-(height/2)
            ey = center+(height/2)
        if(inter==0):
            pygame.draw.line(surface, (0, 0, 255), (i, sy), (i, ey))
        else:
            pygame.draw.line(surface, (0, 255, 255), (i, sy), (i, ey))
        EndAngle -= AngularStep
        naea-=AngularStep
