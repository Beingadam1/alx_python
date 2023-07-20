def reverse_string(string):
    reverse_string = ''
    for str in string:
        reverse_string = str + reverse_string
    return reverse_string

# print(reverse_string("Hello"))
# print(reverse_string(""))
# print(reverse_string("madam"))
# print(reverse_string("Hello, World!"))