#python -m pip install pypng
import png
import math

from Frame import Frame
from Ray import Ray
from Point3D import Point3D
from AreaLight import AreaLight
from Camera import Camera
from Color import Color
from DirectionalLight import DirectionalLight
from Light import Light
from Material import Material
from OrthographicCamera import OrthographicCamera
from PerspectiveCamera import PerspectiveCamera
from PointLight import PointLight
from SceneObject import SceneObject
from Sphere import Sphere
from SpotLight import SpotLight





print("Starting our ray tracer")


# Minimum for a ray tracer
# A frame to render to
# A camera
# A light
# An object to render


frame = Frame(256, 256)

cameraOrigin = Point3D(0,0,1)
origin = Point3D(0,0,0)
cameraLookAt = origin
cameraUp = Point3D(0,1,0)
camreaBackgroundColor = Color(0,0,0)

camera = Camera(cameraOrigin, cameraLookAt, cameraUp, camreaBackgroundColor)

lightDirection = Point3D(0,-1,0)
lightColor = Color(255,255,255)

light = DirectionalLight(lightColor, 1, lightDirection)

sphereCenter = origin
sphereRadius = 1
sphereMaterialColor = Color(255, 0, 0)
sphereMaterialSpecularColor = Color(255,255,255)
sphereMaterialSpecularStrength = 1

sphereMaterial = Material(sphereMaterialColor, sphereMaterialSpecularColor, sphereMaterialSpecularStrength)

sphere = Sphere(sphereMaterial, sphereCenter, sphereRadius)

lights = [light]
objects = [sphere]

#Now loop over every pixel in our frame

#For every pixel
#Figure out where in camera space that pixel is
#Then figure out where in world space that pixel is
#Then shoot a ray from the world space origin of the camera to that world space location
#Then loop over each object in the scene
#For ever object that ray collides with
#Find out which one has the closest collission
#That's our hit
#If we don't have a hit, return the background color
#Then calculate the color based on the direction to the right


    


##Write the buffer out to a file

#Open the output file in binary mode
f = open('./saved.png', 'wb')

#Create a write object
w = png.Writer(frame.width, frame.height, greyscale=False)

#Write to the open file
w.write_array(f, frame.buffer)

#Close the file
f.close()

print("Finished rendering the file")