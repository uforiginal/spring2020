class Frame:
    def __init__(self, width:int, height:int):
        self.buffer = [128 for x in range(width*height*3)]
        self.width = width
        self.height = height
        for h in range(height):
            for w in range(width):
                self.buffer[h*width*3 + w*3] = 255
                self.buffer[h*width*3 + w*3+1] = 128
                self.buffer[h*width*3 + w*3+2] = 255

    def set(self, x, y, r, g, b):
        indexR = y * self.width*3 + x * 3 + 0
        indexG = y * self.width*3 + x * 3 + 1
        indexB = y * self.width*3 + x * 3 + 2
        self.buffer[indexR] = r
        self.buffer[indexG] = g
        self.buffer[indexB] = b