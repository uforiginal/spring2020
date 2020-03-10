import math

class Vector:
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def clone(self):
        return Vector(self.x, self.y, self.z)

    
    def length(self):
        return math.sqrt(self.lengthSquared())

    def lengthSquared(self):
        return self.x ** 2 + self.y **2 + self.z ** 2

    def minus(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return Vector(dx, dy, dz)

    def plus(self, other):
        dx = self.x + other.x
        dy = self.y + other.y
        dz = self.z + other.z
        return Vector(dx, dy, dz)

    def toNormalized(self):
        len = self.length()
        toReturn = self.clone()
        toReturn.x /= len
        toReturn.y /= len
        toReturn.z /= len
        return toReturn

    def toScaled(self, scale:float):
        return Vector(self.x * scale, self.y * scale, self.z * scale)

    def cross(self, other):
        return Vector(self.y*other.z - self.z*other.y, -(self.x*other.z - self.z*other.x), self.x*other.y - self.y*other.x)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    


    