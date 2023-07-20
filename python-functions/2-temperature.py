def convert_to_celsius(fahrenheit):
    output = (fahrenheit - 32) / (9/5)
    return output

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))