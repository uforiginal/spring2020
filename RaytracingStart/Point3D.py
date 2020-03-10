class Point3D:
    def __init__(self, x:float, y:float, z:float):
       self.x = x
       self.y = y
       self.z = z

    def minus(self, point):
        toReturn = Point3D(0,0,0)
        toReturn.x = self.x - point.x
        toReturn.y = self.y - point.y
        toReturn.z = self.z - point.z
        return toReturn

    def dot(self, point):
        x = self.x * point.x
        y = self.y * point.y
        z = self.z * point.z
        return x + y + z
    
