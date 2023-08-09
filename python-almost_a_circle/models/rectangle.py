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
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
