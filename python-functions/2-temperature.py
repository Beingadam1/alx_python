def convert_to_celsius(fahrenheit):
    celsius = (5 / 9 * (fahrenheit - 32))
    return celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))