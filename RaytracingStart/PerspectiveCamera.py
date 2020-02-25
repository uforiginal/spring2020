from Point3D import Point3D
from Camera import Camera

class PerspectiveCamera(Camera):
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D, fov:float):
        Camera.__init__(self, origin, lookAt, up)
        self.fov = fov
      