import math


import math
def calc(FOV,pla,angularStep):
    ########################################################################
    ##   do all calulations before hand so that game runs smooth on python
    ########################################################################

    ####### CALCULATE ALL SIN AND COS FOR ALL POSSIBLE ANGLE FOR THE GAME 
    cs=[]
    si=[]
    i=0
    while i<360:
        cs.append(math.cos(i*math.pi/180))
        si.append(math.sin(i*math.pi/180))
        i+=angularStep


    return(cs,si,len(cs)-1)