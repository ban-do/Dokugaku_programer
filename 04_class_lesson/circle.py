import math

class circle:
    def __init__(self,h):
        self.hl = h

    def area(self):
        pi = math.pi
        return self.hl*self.hl*pi

en = circle(1)
result = en.area()
print(result)
