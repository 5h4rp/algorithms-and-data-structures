# Sorting1234 -> ginortS1324

# First method
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

'''
    - "key" is setting values for each element so as to use them for comparison and subsequently sorting later on.
    - Each parameter in our lambda function contributes to the value of key - the order in which the parameters are aranged has to do with this but I don't know how (help please :D)
    - ord(c) finds the unicode point of the character we're looking at
    - We use >> to shift the ordinal value to less than 2 bits (so between 0 and 3 in decimal) '>>' is binary right shift
    - We set the result of this to a negative because we sort in ascending order

Basically -ord(c) >> 5 sets the values to -3 if it's a lowercase character, -2 if it's an uppercase character and -1 if it's a digit. This segregates each section of our string into uU12. From here we need to sort the numbers, so we use c in '02468' to do so. And then we use c at the end to sort the contents of each group by value.

>>> bin(ord('0'))
'0b0110000'
>>> bin(ord('9'))
'0b0111001'
>>> bin(ord('A'))
'0b1000001'
>>> bin(ord('Z'))
'0b1011010'
>>> bin(ord('a'))
'0b1100001'
>>> bin(ord('z'))
'0b1111010'

The first 2 binary digits will separate the characters into digits, lower case, upper case. So right shifting the value of ord(c) will just give those digits, e.g.

>>> bin(ord('a') >> 5)
'0b11'
which is 3 when represented as int.

'''

# Second
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

# Third
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

# Fourth
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')