import math
import GameEnigneLib.AngleCal as ac

import math
def calc(FOV,pla,angularStep,gr):
    ########################################################################
    ##   do all calulations before hand so that game runs smooth on python
    ########################################################################

    ####### CALCULATE ALL SIN AND COS FOR ALL POSSIBLE ANGLE FOR THE GAME 
    cs=[]
    subcs=[]
    si=[]
    subsi=[]
    angleBeetweenLines=[]
    i=0
    while i<360:
        cs.append(math.cos(i*math.pi/180))
        si.append(math.sin(i*math.pi/180))
        EndAngle=ac.giveAbsAngle(i+FOV)
        naea=i+FOV
        AngularStep = (FOV*2)/gr[0]
        PlayerHeight = 0
        center = (gr[1]/2)-1
        subcs.append([])
        subsi.append([])
        angleBeetweenLines.append([])
        for j in range(0,gr[0]):
            la = EndAngle
            la = ac.giveAbsAngle(la)
            #print("Line Angle :",la)
            ###########################################
            # .    Get perpendicular length
            ###########################################
            abl= 0
            if(naea>i):
                abl=naea-i
            elif(naea<i):
                abl=i-naea
            angleBeetweenLines[i].append(math.cos(abl**math.pi/180))    
            ######calculate line tracer here
            EndAngle -= AngularStep
            naea-=AngularStep
        i+=angularStep

    # precalculate 3d engine and linetracer maths .

    

    return(cs,si,len(cs)-1)