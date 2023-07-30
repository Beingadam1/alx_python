class Square:
    '''class Square that defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module'''

    def __init__(self, size) -> None:
        self.__size = size


Square1 = Square(6)
