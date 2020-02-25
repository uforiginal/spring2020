from Point3D import Point3D
from Camera import Camera
from Color import Color

class PerspectiveCamera(Camera):
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D, backgroundColor:Color, fov:float):
        Camera.__init__(self, origin, lookAt, up, backgroundColor)
        self.fov = fov
      