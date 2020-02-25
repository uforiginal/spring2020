from SceneObject import SceneObject
from Point3D import Point3D
from Material import Material

class Sphere(SceneObject):
    def __init__(self, material:Material, center:Point3D, radius:float):
        SceneObject.__init__(self, material)
        self.center = center
        self.radius = radius