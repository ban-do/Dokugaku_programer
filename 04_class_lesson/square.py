class Square:
    square_list = []

    def __init__(self,l):
        self.len = l
        self.square_list.append(self)

    def __repr__(self):
        return("{} by {} by {} by {}".format(self.len,self.len,self.len,self.len))

sq1 = Square(1)
sq2 = Square(2)
sq3 = Square(3)
#print(Square.square_list[2].len)

print(sq1)

def get_2param(a,b):
    if a is b:
        return True
    else:
        return False

print(get_2param(1,"5"))
print(get_2param(1,2))
print(get_2param(1,1))
