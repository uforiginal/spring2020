#python -m pip install pypng
import png
import math

from Frame import Frame





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