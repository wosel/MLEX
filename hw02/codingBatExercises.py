import re


def frontTimes(str, n):
    """ repeats first three characters of string n times
    from CodingBat -> Warmup 2

    :param str: string to take first 3 chars from
    :param n: number of times to repeat the string
    :returns: first three characters of string repeated n times
    """
    return ''.join([str[:3] for i in range(n)])


def last2(str):
    """ counts the number of times last two chars in string occur elsewhere in the string

    :param str: the string to find the last two chars in and find repetitions of
    :returns: number of repetitions of last two chars in whole string
    """
    return len([m.start() for m in re.finditer('(?=' + str[-2:] + ')', str[0:-1])])


"""
def last2(str):
  ct = 0;
  lookupStr = str[-2:]
  for x in range(len(str)-2):
    if (str[x:x+2] == lookupStr): ct += 1
  return ct

  """

def stringBits(str):
    """ concatenates of every other letter in supplied string
    from CodingBat -> Warmup 2
    :param str: the string to take every other letter from
    :returns: a concatenation of every other letter in supplied string
    """

    indices = [x for x in range(len(str)) if (x % 2 == 0)]
    return ''.join([str[i] for i in indices])

def stringSplosion(str):
    """ concatenates all prefixes of given string, from shortest to longest
    from CodingBat -> Warmup 2

    :param str: the string to take prefixes from
    :returns: concatenation of all prefixes of given string, from shortest to longest
    """
    return ''.join([str[0:x] for x in range(1, len(str)+1, 1)])

def stringTimes(str, n):
    """ repeats the whole string n times
    from CodingBat -> Warmup 2

    :param str: the string to repeat
    :param n: number of times to repeat the string
    :return: the input string repeated n times
    """
    return ''.join([str for i in range(n)])


def arrayCount9(nums):
    """ counts all occurences of 9 in given list
    from CodingBat -> Warmup 2

    :param nums: the list to find 9s in
    :return: number of 9s in list
    """
    return len([i for i, x in enumerate(nums) if x == 9])


def arrayFront9(nums):
    """ looks for a 9 in the first 4 elements of a list
    from CodingBat -> Warmup 2

    :param nums: the list to find the 9 in
    :return: true iff 9 is in first 4 elements of list
    """
    return len([i for i, x in enumerate(nums[0:4]) if x == 9]) > 0


def array123(nums):
    """ looks for the sequence 1, 2, 3 in a list
    from CodingBat -> Warmup 2

    :param nums: list to look in
    :return: True iff sequence 1, 2, 3 occurs in list
    """
    tmp = ',' + (','.join([str(i) for i in nums])) + ','
    return tmp.find(',1,2,3,') >= 0


def stringMatch(a, b):
    """ counts positions where strings a and b contain the same length 2 substring
    from CodingBat -> Warmup 2

    :param a: first string to match
    :param b: second string to match
    :return: number of positions where strings a and b contain the same length substring
    """
    return len([x for x in range(min(len(a), len(b)) - 1) if a[x:x+2] == b[x:x+2]])


def countEvens(nums):
    """ counts even integers in list
    from CodingBat -> List 2

    :param nums: list of integers to count even ones in
    :return: number of even integers in list
    """

    return len([x for x in nums if x % 2 == 0])