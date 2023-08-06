''' Module that check if object is exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    '''
    Parameters:
        obj (object): The object to check.
        a_class (type): The specified class to compare with.

    Returns:
      boolean: True if the object is exactly an instance of the specified class, False otherwise.
    '''
    return type(obj) is a_class
