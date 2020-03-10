import math
from Vector import Vector


class Point3D:
    def __init__(self, x:float, y:float, z:float):
       self.vector = Vector(x,y,z)

    def fromVector(vector:Vector):
        return Point3D(vector.x, vector.y, vector.z)

    def distance(self, other):
        vectorDifference = self.minus(other)
        return vectorDifference.length()

    def minus(self, other):
        return self.vector.minus(other.vector)