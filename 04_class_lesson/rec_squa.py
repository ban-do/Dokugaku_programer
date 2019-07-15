class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.len = l
        self.wide = w

    def calculate_perimeter(self):
        return (self.len+self.wide)*2

class Square(Shape):
    def __init__(self,l):
        self.len = l

    def calculate_perimeter(self):
        return self.len*4

    def change_size(self,l):
        self.len = l


rec1 = Rectangle(3,4)
squ1 = Square(3)
print(rec1.calculate_perimeter())
print(squ1.calculate_perimeter())

squ1.change_size(2)
print("change size is {}".format(squ1.len))

rec1.what_am_i()
squ1.what_am_i()
