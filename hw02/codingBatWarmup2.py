import re

def frontTimes(str, n):
    """ repeats first three characters of string n times

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

    :param str: the string to take every other letter from
    :returns: a concatenation of every other letter in supplied string
    """

    indices = [x for x in range(len(str)) if (x % 2 == 0)]
    return ''.join([str[i] for i in indices])

def stringSplosion(str):
    """ concatenates all prefixes of given string, from shortest to longest

    :param str: the string to take prefixes from
    :returns: concatenation of all prefixes of given string, from shortest to longest
    """
    return ''.join([str[0:x] for x in range(1, len(str)+1, 1)])

def stringTimes(str, n):
    """ repeats the whole string n times

    :param str: the string to repeat
    :param n: number of times to repeat the string
    :return: the input string repeated n times
    """
    return ''.join([str for i in range(n)])
