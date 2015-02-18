def stringBits(str):
    indices = [x for x in range(len(str)) if (x % 2 == 0)]
    return ''.join([str[i] for i in indices])
