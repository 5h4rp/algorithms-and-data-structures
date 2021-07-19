# def appendAtFront(x,L):
#     return [x + element for element in L]

# def bitStrings(n):
#     if n == 0:
#         return []
#     if n == 1:
#         return ["0","1"]
#     else:
#         return (appendAtFront("0", bitStrings(n-1)) + appendAtFront("1", bitStrings(n-1)))

# print(bitStrings(4))

####################################################################

def bitStrings2(n):
    if n == 0:
        return []
    if n == 1:
        return ["0","1"]
    return [digit + bitString for digit in bitStrings2(1) for bitString in bitStrings2(n-1)]

print(bitStrings2(4))