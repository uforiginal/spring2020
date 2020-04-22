from Point3D import Point3D
from Vector import Vector

class Camera:
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D, backgroundColor:Vector, raysPerPixel:int):
       self.origin = origin
       self.lookAt = lookAt
       self.up = up
       self.backgroundColor = backgroundColor
       self.raysPerPixel = raysPerPixel