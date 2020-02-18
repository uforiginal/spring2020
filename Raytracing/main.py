#python -m pip install pypng
import png
import math

from math_helper import *
from setup import *
from renderer import *

from Frame import *
from Camera import *
from EnvironmentMap import *




print("Starting our ray tracer")


    
r=png.Reader("background.png")
temp = r.read()
EnvironmentMap.backgroundData = list(temp[2])
EnvironmentMap.backgroundWidth = temp[0]
EnvironmentMap.backgroundHeight = temp[1]
print(f'The background image has dimensions {str(temp[0])}, {str(temp[1])}')

## Run the ray tracing algorithm
run()

#Write the buffer out to a file

#Open the output file in binary mode
f = open('./saved.png', 'wb')

#Create a write object
w = png.Writer(Frame.width, Frame.height, greyscale=False)

#Write to the open file
w.write_array(f, Frame.buffer)

#Close the file
f.close()

print("Finished rendering the file")