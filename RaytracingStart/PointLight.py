from Light import Light
from Color import Color
from Point3D import Point3D

class PointLight(Light):
    def __init__(self, color:Color, strength:float, position:Point3D):
        Light.__init__(self, color, strength)
        self.position = position