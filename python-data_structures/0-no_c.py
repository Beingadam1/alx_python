def no_c(my_string):
    new_string = ''
    for str in my_string:
        if str.lower() != 'c':
            new_string += str
    return new_string

