from Light import Light
from Color import Color
from Point3D import Point3D
from SceneObject import SceneObject

class AreaLight(Light):
    def __init__(self, color:Color, strength:float, sceneObject:SceneObject):
        Light.__init__(self, color, strength)
        self.sceneObject = sceneObject