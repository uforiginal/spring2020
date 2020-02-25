from SceneObject import SceneObject
from Point3D import Point3D

class Sphere(SceneObject):
    def __init__(self, center:Point3D, radius:float):
        SceneObject.__init__(self)
        self.center = center
        self.radius = radius