raise_exception_msg = __import__("5-raise_exception_msg").raise_exception_msg

try:
    raise_exception_msg("")
except NameError as ne:
    print(ne)
