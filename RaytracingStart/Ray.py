from Point3D import Point3D

class Ray:
    def __init__(self,origin : Point3D, direction : Point3D):
        self.origin = origin
        self.direction = direction