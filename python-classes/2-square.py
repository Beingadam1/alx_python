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

    def area(self):
        '''
        Determine the area of the square
        Returns: The square of the size
        '''
        return self.__size**2
