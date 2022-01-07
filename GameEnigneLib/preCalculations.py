import math
import GameEnigneLib.AngleCal as ac

import math

from GameEnigneLib.lineTracer import checkY
def calc(FOV,pla,angularStep,gr):
    ########################################################################
    ##   do all calulations before hand so that game runs smooth on python
    ########################################################################

    ####### CALCULATE ALL SIN AND COS FOR ALL POSSIBLE ANGLE FOR THE GAME 
    
    ####################################
    #  Update Function Calculations
    ####################################
    cs=[]
    si=[]
    ###################################

    ###################################
    # 3D RENDERER CALCUALTIONS
    ###################################
    angleBeetweenLines=[]
    lineAngle=[]


    ###################################
    #   LINE TRACER CALCULATIONS
    ###################################
    dy=[]
    dx=[]
    llpy=[]
    llpx=[]



    i=0
    ic=0
    index=0
    while i<360:

        if(ic==0,ic==45,ic==90,ic==135,ic==180,ic==225,ic==270,ic==315):
            i=ic+0.001

        ##### UPDATE FUNCTION
        cs.append(math.cos(i*math.pi/180))
        si.append(math.sin(i*math.pi/180))

        EndAngle=ac.giveAbsAngle(i+FOV)
        naea=i+FOV
        AngularStep = (FOV*2)/gr[0]
        PlayerHeight = 0
        center = (gr[1]/2)-1
        lineAngle.append([])
        angleBeetweenLines.append([])
        dy.append([])
        dx.append([])
        llpy.append([])
        llpx.append([])


        for j in range(0,gr[0]):
            la = EndAngle
            la = ac.giveAbsAngle(la)
            lineAngle[index].append(la)
            #print("Line Angle :",la)



            ###########################################
            # .    Get perpendicular length
            ###########################################
            abl= 0
            if(naea>i):
                abl=naea-i
            elif(naea<i):
                abl=i-naea
            angleBeetweenLines[index].append(math.cos(abl*math.pi/180))




            ######calculate line tracer here
            dy[index].append(math.sin(la*math.pi/180))
            dx[index].append(math.cos(la*math.pi/180))
            llpy[index].append(abs( 1/math.sin(la*math.pi/180)))
            llpx[index].append(abs(1/math.cos(la*math.pi/180)))

            EndAngle -= AngularStep
            naea-=AngularStep
        ic+=angularStep
        index+=1
    # precalculate 3d engine and linetracer maths .
    return(cs,si,len(cs)-1,angleBeetweenLines,lineAngle,dy,dx,llpy,llpx,angularStep)