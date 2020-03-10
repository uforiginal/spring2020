from Point3D import Point3D
from Vector import Vector

class Ray:
    def __init__(self,origin : Point3D, direction : Vector):
        self.origin = origin
        self.direction = direction

    