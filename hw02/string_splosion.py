def stringSplosion(str):
    return ''.join([str[0:x] for x in range(1, len(str)+1, 1)])
