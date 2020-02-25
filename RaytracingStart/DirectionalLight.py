from Light import Light
from Color import Color
from Point3D import Point3D

class DirectionalLight(Light):
    def __init__(self, color:Color, strength:float, direction:Point3D):
        Light.__init__(self, color, strength)
        self.direction = direction