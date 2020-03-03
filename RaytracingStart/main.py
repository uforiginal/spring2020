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
from OrthographicCamera import OrthographicCamera
from PerspectiveCamera import PerspectiveCamera
from PointLight import PointLight
from SceneObject import SceneObject
from Sphere import Sphere
from SpotLight import SpotLight





print("Starting our ray tracer")

frame = Frame(256, 256)




for y in range(256):
    for x in range(256):
        #Pattern to move between reference spaces
        #1. Divide by maximum value
        #2. Subract by .5 so I'm centered about 0
        #3. Multiply by the biggest number * 2 in the new space
        cameraX = x/255 #1.
        cameraX = cameraX -.5 #2.
        cameraX = cameraX * 2 #3.

        cameraY = y/255
        cameraY = cameraY - .5
        cameraY = cameraY * 2
        cameraY = cameraY * -1 #Account for flipped Y

        pixelX = cameraX #Just because we set it up right
        pixelY = cameraY 
        pixelZ = 0

        originX = 0
        originY = 0
        originZ = 1

        sadDirectionX = pixelX - originX
        sadDirectionY = pixelY - originY
        sadDirectionZ = pixelZ - originZ

        lengthSad = math.sqrt(sadDirectionX*sadDirectionX + sadDirectionY*sadDirectionY + sadDirectionZ * sadDirectionZ)

        directionX = sadDirectionX / lengthSad
        directionY = sadDirectionY / lengthSad
        directionZ = sadDirectionZ / lengthSad

        origin = Point3D(originX, originY, originZ)
        direction = Point3D(directionX, directionY, directionZ)
        center = Point3D(0,0,0)
        radius = .5

        e = origin.minus(center)
        a = direction.dot(direction)
        b = 2*direction.dot(e)
        c = e.dot(e)-radius*radius

        discriminant = b*b - 4 * a * c
        if discriminant < 0:
            frame.buffer[y*256*3] = 0
            frame.buffer[y*256*3+1] = 0
            frame.buffer[y*256*3+2] = 0











    


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