import math
from math_helper import *
from Frame import *
from Camera import *
from Objects import *
from Lights import *

## Setup functions for the environment
def simpleSetup():
  centers = [[0, 0, -1],[.5,0,-1]]                 #The center of the circle
  rs = [.5,.5]                              #The radius of the circle
  circleColors = [[255,255,0],[255,0,0]]               #The diffuse color of the circle
  return [centers, rs, circleColors]

def simplest():
  centers = [[0, 0, -1]]                 #The center of the circle
  rs = [.5]                              #The radius of the circle
  circleColors = [[255,255,255]]               #The diffuse color of the circle
  return [centers, rs, circleColors]

def more():
  centers = [[0,-1.5,-1],[0,0,-1],[.5,.5,-1],[0,.5,-1],[-.5,.5,-1]]
  rs=[1,.25,.125, .125,.125]
  circleColors=[[255,0,0],[0,255,0],[255,0,255],[0,255,255],[255,255,0]]
  return [centers, rs, circleColors]

# Setup our output image
Frame.width = 256
Frame.height = 256

Frame.buffer = [128 for x in range(Frame.width*Frame.height * 3)]   #Where we store our pixel data


#Setup our camera
Camera.cameraLoc = [0,0,0]                 #Where the camera is looking from
Camera.cameraLookAt = [0,0,-1]             #Where the camera is looking at
Camera.cameraHalfAngle = math.pi/2         #The half width of the field of view
Camera.extent = math.sin(Camera.cameraHalfAngle)  # Given our field of view, what is the half height of our field of view at our look at point?
Camera.doubleExtent = Camera.extent * 2           #Given our field of view, what is the full height at our look at point?

Camera.backgroundColor = [0, 0, 0]       #The background color, or the color we use if our ray doesn't hit anything

Lights.lightDirection = [0,1,0]            #The direction to an infinitely distant light source (e.g. sun)
Lights.lightDirection = normalized(Lights.lightDirection)

Lights.ambient = [25,25,25]

#Information about our circle

#[centers, rs, circleColors] = [[],[],[]]
[Objects.centers, Objects.rs, Objects.circleColors] = simplest()
#[centers, rs, circleColors] = simpleSetup()
#[centers, rs, circleColors] = more()