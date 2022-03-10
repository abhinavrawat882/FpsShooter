import GameEnigneLib.AngleCal as ac
import GameEnigneLib.lineTracer as lt
import math
rd = 0.0174533
def threDRenderer(x, y, surface,pygame,gr,la,abl,index,dy,dx,llpy,llpx,mp):
    lineTracer=lt.lineTracer
    # Define Variable :-
    #######################################
    #   Precalculate these 
    #######################################
    gh = gr[1]
    gw = gr[0]
    wallHeightMul=2
    PlayerHeight = 0
    center = (gh/2)-1
    
  
    ############################################
    #             FRAME DRAWING
    ###########################################

    for i in range(0, gw):

        ###########################################
        # .    Get line length
        ###########################################
        
        ln,inter,xe,ye = lineTracer(x, y, la[index][i], mp,dy[index][i],dx[index][i],llpy[index][i],llpx[index][i])
        
        #enemy info template

        #each enemy data template
        #[TYPE OF ENEMY,ln,c1,c2,x,y]
        

        ###########################################
        # .    Get perpendicular length
        ###########################################
     
        #print("Angle Beetween  :",angleBeetweenLines)
        ln = ln*abl[index][i]
        

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

