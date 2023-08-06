'''
    Check if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.
'''


def inherits_from(obj, a_class):
    """


    Parameters:
        obj (object): The object to check.
        a_class (type): The specified class to compare with.

    Returns:
        boolean: True if the object is an instance of a class that
        inherited from the specified class, False otherwise.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
