from Color import Color

class Material:
    def __init__(self, diffuseColor:Color, specularColor:Color, specularStrength:float):
        self.diffuseColor = diffuseColor
        self.specularColor = specularColor
        self.specularStrength  = specularStrength