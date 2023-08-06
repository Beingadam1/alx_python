''' Module if the object is an instance of, 
or if the object is an instance of a class 
that inherited from, the specified class'''


def is_kind_of_class(obj, a_class):
    '''
    Parameters:
        obj (object): The object to check.
        a_class (type): The specified class to compare with.

    Returns:
      boolean:  True if the object is an instance of the specified class
      or its subclass, False otherwise.
    '''
    return isinstance(obj, a_class)
