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