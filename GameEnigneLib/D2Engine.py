# 2D Engine
import GameEnigneLib.AngleCal as ac
import math
import GameEnigneLib.lineTracer as lt

def miniMapRenderer(screen2d, x, y, a, pygame, mp,gr,mmr):
    mml=10
    ################################
    #       RENDER MAP
    ################################
    factor = mmr[0]/mml
    x1,y1=ac.CorToMat(int(x),int(y),len(mp))
    for i in range(y1-5,y1+5,1):
        if(i>=0 and i<len(mp[0])):
            for j in range(x1-5,x1+5,1):
                
                if(j>=0 and j<len(mp)):
                    if( mp[i][j] == 1):
                        pygame.draw.rect(screen2d, (255, 255, 255), pygame.Rect(
                            gr[0]-58+j*factor-10,i*factor+10, factor, factor))

    #####################################
    # Render player
    #####################################

    #xi, yi = ac.CorToSrc(x, y, 16)
    #pygame.draw.circle(screen2d, (225, 0, 0), (xi*factor, yi*factor), 5)

    #####################################
    #         Render Line
    #####################################

    # Calculate point of line
    
    #i=a-29
    #while(i<a+29):
    #    ln,inter,xe,ye = lineTracer(x, y, ac.giveAbsAngle(i), mp)
    #    endx, endy = ac.CorToSrc(xe, ye, 16)
    #    pygame.draw.line(screen2d, (255, 255, 255), (xi*factor,yi*factor), (endx*factor, endy*factor))
    #    i+=1
    #ln,inter,xe,ye = lineTracer(x, y, a, mp)
    #endx, endy = ac.CorToSrc(xe, ye, 16)
    #pygame.draw.line(screen2d, (255, 255, 255), (xi*factor,yi*factor), (endx*factor, endy*factor))
    