def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result

def baseKStrings(n,k):
    if n == 0:
        return []
    if n == 1:
        return rangeToList(k)
    return [digit+bistring for digit in baseKStrings(1,k) for bistring in baseKStrings(n-1,k)]

print(baseKStrings(2,4))