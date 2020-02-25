from Point3D import Point3D
from Camera import Camera

class OrthographicCamera(Camera):
    def __init__(self, origin:Point3D, lookAt:Point3D, up:Point3D, halfWidth:float, halfHeight:float):
        Camera.__init__(self, origin, lookAt, up)
        self.halfWidth = halfWidth
        self.halfHeight = halfHeight
      