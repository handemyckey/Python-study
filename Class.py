#Creating Class and object and calling functions using object
class Rectangle:
    def __init__(self,width,height):
        self._width = width         # setting _width as private variable
        self._height = height       # setting _height as private variable

    @property
    def width(self):
        return self._width

    @width.setter               #setting the width value by checking it is positive or not
    def width(self, width):
        if width <= 0:
            raise ValueError("Width Must Be Positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter               #setting the height value by checking it is positive or not
    def height(self, height):
        if height <= 0:
            raise ValueError("Height Must Be Positive.")
        else:
            self._height = height

    def area(self):
        test =  self.width * self.height
        print(test)

    def perimiter(self):
        test_1 =  2 * (self.width + self.height)
        print(test_1,'\n')

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            sample = self.width == other.width and self.height == other.height
            print(sample)
        else:
            print("False")
r1 = Rectangle(100,20)
r2 = Rectangle(10,20)


print(r1 is not r2)
print(r1 == r2)


r1.area()
r1.perimiter()

r2.area()
r2.perimiter()

