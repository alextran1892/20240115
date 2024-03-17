input_string = input('Entry String to count char: ')

def count_chars(input_string):
    result = 0
    for char in input_string:
        result += 1
    return result

print(input_string)
print('Lengt of input_string: ', count_chars(input_string))

