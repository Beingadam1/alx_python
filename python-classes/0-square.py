'''
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
'''


class Square:
    '''Represents a square'''

    def __init__(self, size) -> None:
        '''Initializing this square class
        Args: size - represnets the size of the square defined
        '''
        self.__size = size
