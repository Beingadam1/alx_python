'''
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0) -> None:
        '''Initializing this square class
        Args: size - represnets the size of the square defined
        Raises: TypeError: if size is not integer
                ValueError: if size is less than zero
        '''

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        '''Retrieves size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        """
        value: validates the value of the size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        '''
        Determine the area of the square
        Returns: The square of the size
        '''
        return self.__size**2

    def my_print(self):
        '''prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
