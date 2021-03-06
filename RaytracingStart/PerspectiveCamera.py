from Point3D import Point3D
from Camera import Camera
from Vector import Vector

class PerspectiveCamera(Camera):
    """ A camera represented a physical camera or eye. """
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D, backgroundColor:Vector, raysPerPixel: int, focusPoint: float, fov:float):
        Camera.__init__(self, origin, lookAt, up, backgroundColor, raysPerPixel)
        self.focusPoint = focusPoint
        self.fov = fov
      