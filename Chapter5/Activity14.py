    ## Activity 14 – creating classes and inheriting from a parent class
    
class Polygon:
    """
    This is the parent class that represents a polygon.
    """
    def __init__(self, num_sides):
        self.num_sides = num_sides

    @property
    def perimeter(self):
        """
        This property returns the perimeter of the polygon.
        """
        raise NotImplementedError

    def __str__(self):
        """
        This method returns a string representation of the polygon.
        """
        return f"polygon with {self.num_sides} sides"


class Rectangle(Polygon):
    """
    This is a child class that represents a rectangle.
    """
    def __init__(self, height, width):
        super().__init__(num_sides=4)
        self.height = height
        self.width = width

    @property
    def perimeter(self):
        """
        This property returns the perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)

    @property
    def area(self):
        """
        This property returns the area of the rectangle.
        """
        return self.height * self.width


class Square(Rectangle):
    """
    This is a child class that represents a square.
    """
    def __init__(self, side_length):
        super().__init__(height=side_length, width=side_length)


# Create a rectangle object
r = Rectangle(5, 12)
print((r.area, r.perimeter))  # Output: (60, 34)

# Create a square object
s = Square(5)
print((s.area, s.perimeter))  # Output: (25, 20)
