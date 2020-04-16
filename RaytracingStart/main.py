#python -m pip install pypng
import png
import math
import Point3D

from Frame import Frame



print("Starting our ray tracer")
frame = Frame(256, 256)
directionalLightX = 0
directionalLightY = -1
directionalLightZ = 0



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
        else :
            

        if t<0:
            frame.buffer[y*256*3 + x*3] = 0
            frame.buffer[y*256*3 + x*3+1] = 0
            frame.buffer[y*256*3 + x*3+2] = 0
        else:
            ambient = 0
            diffuse = 0
            specular = 0

            collisionX = directionX * t + originX
            collisionY = directionY * t + originY
            collisionZ = directionZ * t + originZ

            uNNx = collisionX - center.x
            uNNy = collisionY - center.y
            uNNz = collisionZ - center.z

            normalLength = math.sqrt(uNNx**2 + uNNy**2 + uNNz**2)
            circleNormalx = uNNx/normalLength
            circleNormaly = uNNy/normalLength
            circleNormalz = uNNz/normalLength

            toLightX = -directionalLightX
            toLightY = -directionalLightY
            toLightZ = -directionalLightZ

            dotProduct = circleNormalx*toLightX + circleNormaly*toLightY + circleNormalz*toLightZ
            if dotProduct < 0:
                dotProduct = 0

            diffuseR = 255 * dotProduct
            diffuseG = 255 * dotProduct
            diffuseB = 255 * dotProduct

            cR = math.floor(ambient + diffuseR + specular)
            cG = math.floor(ambient + diffuseG + specular)
            cB = math.floor(ambient + diffuseB + specular)
            if cR>255:
                cR = 255
            if cG>255:
                cG = 255
            if cB>255:
                cB = 255

            frame.buffer[y*256*3 + x*3] = c
            frame.buffer[y*256*3 + x*3+1] = c
            frame.buffer[y*256*3 + x*3+1] = c

            #I need a normal
            #I need the light direction
            #I need the dot product















    
for y in range(256):
    for x in range(256):
        #pattern to move between ref spaces
        #1) divide by maximum value
        #2) subtract by .5 so I am centered about 0
        #3) multiply by the biggest number * 2 in the new space
        cameraX = x/255 #1)
        cameraX = cameraX - 0.5 #2)
        cameraX = cameraX * 2 #3)

        cameraY = y/255
        cameraY = cameraY - 0.5
        cameraY = cameraY *2
        cameraY = cameraY * -1 #accounts for flipped Y

        pixelX = cameraX
        pixelY = cameraY
        pixelZ = 0

        originX = 0
        originY = 0
        originZ = 1

        #whenever we have a drection, we want a unit vector
        # normalizing : the process of turning a vactor into a unit vector
            #1) get length (length != 1)
            #2) divide by length
            #3) length = sqrt(x^2+y^2+z^2)
            #4) (x/length, y/length, z/length)

        sadDirectionX = pixelX - originX
        sadDirectionY = pixelY - originY
        sadDirectionZ = pixelZ - originZ

        lengthSad = math.sqrt((sadDirectionX*sadDirectionX) + (sadDirectionY*sadDirectionY) + (sadDirectionZ*sadDirectionZ))
        directionX = sadDirectionX / lengthSad
        directionY = sadDirectionY/ lengthSad
        directionZ = sadDirectionZ/ lengthSad

        #sphere definition: (x - centerx)^2 + (y - centery)^2 + (z - centerz)^2 = radius^2
        #ray definition: (origin + direction(time))
        #ray+sphere : (o + dt - c)^2 - r^2 = o
        #if o <0 then we don't intersect the sphere, so we can just abandon it

        origin = Point3D(originX, originY, originZ)
        direction = Point3D(directionX, directionY, directionZ)
        center = Point3D(0,0,0)
        radius = 0.5

        e = origin.minus(center)
        a = direction.dot(direction)
        b = 2*direction.dot(e)
        c = e.dot(e)-radius*radius

        discriminant = b*b - 4 *a *c
        if discriminant < 0:
            frame.buffer[y*256*3] = 0
            frame.buffer[y*256*3+2: int
            frame.buffer[y*256*3 +2] = 0
            


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