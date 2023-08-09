'''A base class'''


class Base:
    '''
    Base class Method:
        __init__: Initialises the class with id(int),
                  Increment __nb_objects.
    Attributes:
        __nb_objects: Initial value = 0
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
