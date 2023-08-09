'''A rectangle class that inherit from the Base class'''

from models.base import Base


class Rectangle(Base):
    '''
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate position of the rectangle.
        y (int): The y-coordinate position of the rectangle.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializing.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position of the rectangle. Default is 0.
            y (int, optional): The y-coordinate position of the rectangle. Default is 0.
            id (int, optional): The unique identifier. Inherits from Base class.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            '''Get the width'''
            return self.__width

        @width.setter
        def width(self, new_width):
            """Set the and Validates width."""
            if type(new_width) is not int:
                raise TypeError("width must be an integer")
            if new_width <= 0:
                raise ValueError("width must be greater than 0")
            self.__width = new_width

        @property
        def height(self):
            """Get the height"""
            return self.__height

        @height.setter
        def height(self, new_height):
            """Set the and Validates height."""
            if type(new_height) is not int:
                raise TypeError("height must be an integer")
            if new_height <= 0:
                raise ValueError("height must be greater than 0")
            self.__height = new_height

        @property
        def x(self):
            """Get the x-coordinate"""
            return self.__x

        @x.setter
        def x(self, new_x):
            """Set the x-coordinate and Validates x."""
            if type(new_x) is not int:
                raise TypeError("x must be an integer")
            if new_x < 0:
                raise ValueError("x must be greater than or equal to 0")
            self.__x = new_x

        @property
        def y(self):
            """Get the y-coordinate"""
            return self.__y

        @y.setter
        def y(self, new_y):
            """Set the y-coordinate and Validates y."""
            if type(new_y) is not int:
                raise TypeError("y must be an integer")
            if new_y < 0:
                raise ValueError("y must be greater than or equal to 0")
            self.__y = new_y
