'''Rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializing

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
        '''Set the width'''
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        '''Get the height'''

        return self.__height

    @height.setter
    def height(self, new_height):
        '''Set the height'''
        if type(new_height) is not int:
            raise TypeError("width must be an integer")
        if new_height <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_height
        self.__height = new_height

    @property
    def x(self):
        '''Get the x position'''

        return self.__x

    @x.setter
    def x(self, new_x):
        '''Set the x position'''
        if type(new_x) is not int:
            raise TypeError("width must be an integer")
        if new_x <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_x
        self.__x = new_x

    @property
    def y(self):
        '''Get the y position'''

        return self.__y

    @y.setter
    def y(self, new_y):
        '''Set the y position'''
        if type(new_y) is not int:
            raise TypeError("width must be an integer")
        if new_y <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_y
        self.__y = new_y
