import math
from math_helper import *
from setup import *
from EnvironmentMap import *
from Camera import *
from Frame import *
from Objects import *
from Lights import *

# Set a pixel to a certain color at a certain point
# This requires a little math since we keep colors in a 1D array
# with three entries, [R,G,B] for each pixel
def setColor(x,y,color):
  Frame.buffer[y*(Frame.width*3)+x*3] = clamp(color[0])
  Frame.buffer[y*(Frame.width*3)+x*3 + 1] = clamp(color[1])
  Frame.buffer[y*(Frame.width*3)+x*3 + 2] = clamp(color[2])


#Main ray tracing function
#3 cases:
# negative determinant - return -1
# Invalid t - return -1
# valid t - return t
def traceRay(d,o, center, r):
    a = dot(d,d)
    b = 2 * dot(d,sub(o,center))
    c = dot(sub(o,center),sub(o,center)) - (r*r)
    discriminant = b*b-4*a*c
    if discriminant > 0:
        isValid = False
        t1 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        t2 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        
        if t1 < 0 and t2 < 0:
            isValid = False
        if min(t1,t2) < 0 and max(t1,t2) > 0:
            isValid = False
        if t1 > 0 and t2 > 0:
            isValid = True
        if not isValid:
            return -1
        else:
            t = min(t1,t2)
            return t
    else:
        return -1

def getTraceRay(d, o, centers, rs):
  closestT = 1000000
  closestI = -1
  
  for i in range(0,len(centers)):
      center = centers[i]
      r = rs[i]
      
      t = traceRay(d, o, center, r)
      
      if t > 0 and t < closestT:
          closestT = t
          closestI = i

  if closestI == -1:
    return [100000, -1, [0,0,0], [0,0,0]]
  
  collision = add(o,mult(d,closestT))
  normal = sub(collision,centers[closestI])
  normal = normalized(normal)
        
  return [closestT, closestI, collision, normal]

def calculateDiffuseColor(d, o, t, i, centers, circleColors, lightDirection):
  collision = add(o,mult(d,t))
  center = centers[i]
  circleColor = circleColors[i]
  normal = sub(collision,center)
  normal = normalized(normal)
  lightIntensity = max(0,dot(normal,lightDirection))

  #Send out a shadwow ray
  #But only if the light intensity > 0
  inShadow = True
  if lightIntensity > 0:
    d = lightDirection
    o = add(collision, mult(lightDirection, .01))
    [closestT, closestI, tempCollision, tempNormal] = getTraceRay(d, o, Objects.centers, Objects.rs)
    
    if closestI == -1:
      inShadow = False

    
  diffuseComponent = [0,0,0]
  if not inShadow:
    diffuseComponent = mult(circleColor, lightIntensity)
  totalDiffuseColor = add(diffuseComponent, Lights.ambient)

  return totalDiffuseColor
      

#Go through and do the ray tracing
def run():
  for y in range(Frame.width):             #Loop over the rows
    for x in range(Frame.width):            #Loop over the columns
      
      #Calculate the un-normalize direction of our ray
      worldZ = Camera.cameraLookAt[2]       #Clearly, we are pointing at the look at Z coordinate
      
      #interpolate to figure out where we are looking in x and y
      worldX = x/Frame.width*2 - 1
      worldY = y/Frame.width*2 - 1
      worldY = worldY * - 1
      
      worldVector = [worldX, worldY, worldZ]
      pixelVector = sub(worldVector, Camera.cameraLoc)
      pixelVector = normalized(pixelVector)
      
      [closestT, closestI, collision, normal] = getTraceRay(pixelVector, Camera.cameraLoc, Objects.centers, Objects.rs)
              
      if closestI < 0:
          #setColor(x,y,backgroundColor)
          setColor(x,y,getBackground(pixelVector))
      else:
         

          totalDiffuseColor = calculateDiffuseColor(pixelVector, Camera.cameraLoc, closestT, closestI, Objects.centers, Objects.circleColors, Lights.lightDirection)

          #Do the reflection 
          reflection = sub(pixelVector, mult(normal, dot(normal, pixelVector)*2))
          reflectionColor = getBackground(reflection)
          [closestT, closestI, tempCollision, tempNormal] = getTraceRay(reflection, add(collision, mult(reflection, 0)), Objects.centers, Objects.rs)
          if closestI != -1:
            #reflectionColor = circleColors[closestI]
            reflectionColor = calculateDiffuseColor(reflection, add(collision, mult(reflection, .01)), closestT, closestI, centers, circleColors, lightDirection)

          finalColor = add(mult(totalDiffuseColor, .5), mult(reflectionColor, .5))
          setColor(x,y,finalColor)

def getBackgroundPixel(x,y):
  y = min(EnvironmentMap.backgroundHeight-1,y)
  y = max(0,y)

  y = EnvironmentMap.backgroundHeight - y

  x = min(EnvironmentMap.backgroundWidth-1,x)
  x = max(0,x)


  r = list(EnvironmentMap.backgroundData[y])[x*4]
  g = list(EnvironmentMap.backgroundData[y])[x*4+1]
  b = list(EnvironmentMap.backgroundData[y])[x*4+2]
  return [r,g,b]

def getBackground(d):
  angle = math.atan2(d[2],d[0])
  lat = (d[1]+1)/2
  return getBackgroundPixel(math.ceil((angle+math.pi)/(2*math.pi)*EnvironmentMap.backgroundWidth),math.ceil(lat*EnvironmentMap.backgroundHeight))

