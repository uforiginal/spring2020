from Point3D import Point3D

class Camera:
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D):
       self.origin = origin
       self.lookAt = lookAt
       self.up = up