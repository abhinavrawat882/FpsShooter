import GameEnigneLib.AngleCal as ac
import math
rd = 0.0174533


def checkY(x, y, Levelmap,a,inte):
    
    #print("Intercept : ",inte)
    x = int(x)
    #print("ABS Y : ",y)
    y = len(Levelmap)-1-y
    y=int(y)
    
    #print("MAT Y :",y)
    if(inte==0):
        if(a<180 and a>0):
            y-=1

        #else:
        #    y+=1
    if(inte==1):
        if(a>90 and a<270):
            x-=1
    elif(inte==2):
        if(a<90 and a>0):
            y-=1
        elif(a>90 and a<180):
            y-=1
            x-=1
        elif(a>180 and a<270):
            x-=1
        elif(a<360 and a>270):
            y==y
    if(x>=len(Levelmap[0]) or y >=len(Levelmap)):
        return True
    #if(inte==2):
        #print("Intercept")
    #print("MatLoc :")
    #print( y,x)
    try:
        if(Levelmap[y][x] > 0):
            return True
        else:
            return False
    except:
        #print("Here")
        #print("loc :",x,y)
        #print("Angle ",a)
        return True


def lineTracer(x, y,lineAngle, Levelmap, dy,dx,llpy,llpx):  # 4.0
    #print("Player Position")
    #print("X: ", x, " Y: ", y, " ANGLE: ", lineAngle)
    
    dely = 0
    delx = 0
    mdy = y % 1
    mdx = x % 1
    if(lineAngle > 0 and lineAngle < 90):
        
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0
    elif(lineAngle > 90 and lineAngle < 180):
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
        else:
            delx = 0
    elif(lineAngle > 180 and lineAngle < 270):
        if(mdy > 0):
            dely = -1*(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
        else:
            delx = 0
    elif(lineAngle > 270 and lineAngle < 360):
        if(mdy > 0):
            dely = -1*(y % 1)

        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0

    lineLen = 0
    tllpy = abs(llpy*dely)
    tllpx = abs(llpx*delx)
    intercept=-1
    while True:
        if(tllpy < tllpx):
            lineLen += tllpy
            tllpx -= tllpy
            x += tllpy*dx
            y += tllpy*dy
            tllpy = llpy
            intercept=0
        elif(tllpy > tllpx):
            lineLen += tllpx
            tllpy -= tllpx
            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            intercept=1
        else:
            lineLen += tllpx
            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            tllpy = llpy
            intercept=2
        #print("CRR")
        #print("X: ", x, " Y: ", y)
        #if lineLen>100:
        #    return lineLen,intercept,x,y
        IsIntercepted=checkY(x, y, Levelmap,lineAngle,intercept)
        if IsIntercepted:
            break
    #print("Line Length", lineLen)
    #print("Line Rendered")
    return lineLen,intercept,x,y
