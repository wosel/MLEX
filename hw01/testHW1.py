import unittest
import codingBatExercises as cb

__author__ = 'Jakub'

class TestHW1(unittest.TestCase):
    name = 'Homework 1 tests'
    description = 'Test for CodingBat exercises in codingBatExercises.py'


    def testFrontTimes(self):
        testList = [
            {'orig': 'Chocolate', 'repeat': 3, 'expResult': 'ChoChoCho'},
            {'orig': 'Chocolate', 'repeat': 2, 'expResult': 'ChoCho'},
            {'orig': 'Abc', 'repeat': 3, 'expResult': 'AbcAbcAbc'},
            {'orig': 'Ab', 'repeat': 4, 'expResult': 'AbAbAbAb'},
            {'orig': 'A', 'repeat': 4, 'expResult': 'AAAA'},
            {'orig': '', 'repeat': 4, 'expResult': ''},
            {'orig': 'Abc', 'repeat': 0, 'expResult': ''}
        ]

        for x in testList:
            actResult = cb.frontTimes(x['orig'], x['repeat'])
            print '\nExpected: frontTimes(\'{orig}\', {repeat}) -> \'{expResult}\''.format(orig=x['orig'], repeat=x['repeat'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testStringTimes(self):
        testList = [
            {'orig': 'Hi', 'repeat': 3, 'expResult': 'HiHiHi'},
            {'orig': 'Chocolate', 'repeat': 2, 'expResult': 'ChocolateChocolate'},
            {'orig': 'Abc', 'repeat': 1, 'expResult': 'Abc'},
            {'orig': 'Abc', 'repeat': 0, 'expResult': ''},
            {'orig': 'Oh, boy!', 'repeat': 2, 'expResult': 'Oh, boy!Oh, boy!'},
            {'orig': '', 'repeat': 4, 'expResult': ''}
        ]
        for x in testList:
            actResult = cb.stringTimes(x['orig'], x['repeat'])
            print '\nExpected: stringTimes(\'{orig}\', {repeat}) -> \'{expResult}\''.format(orig=x['orig'], repeat=x['repeat'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testStringBits(self):
        testList = [
            {'orig': 'Hello', 'expResult': 'Hlo'},
            {'orig': 'Hi', 'expResult': 'H'},
            {'orig': 'Heeololeo', 'expResult': 'Hello'},
            {'orig': '', 'expResult': ''},
            {'orig': 'Hello Kitten', 'expResult': 'HloKte'}
        ]
        for x in testList:
            actResult = cb.stringBits(x['orig'])
            print '\nExpected: stringBits(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testStringSplosion(self):
        testList = [
            {'orig': 'Code', 'expResult': 'CCoCodCode'},
            {'orig': 'x', 'expResult': 'x'},
            {'orig': '', 'expResult': ''},
            {'orig': 'fade', 'expResult': 'ffafadfade'}
        ]
        for x in testList:
            actResult = cb.stringSplosion(x['orig'])
            print '\nExpected: stringBits(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testLast2(self):
        testList = [
            {'orig': 'hixxhi', 'expResult': 1},
            {'orig': 'hixhixhi', 'expResult': 2},
            {'orig': 'hixhixhi', 'expResult': 2}
        ]
        for x in testList:
            actResult = cb.last2(x['orig'])
            print '\nExpected: stringBits(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testArrayCount9(self):
        testList = [
            {'orig': [], 'expResult': 0},
            {'orig': [9, 9, 9], 'expResult': 3},
            {'orig': [1, 2, 9, 1, 9, 3], 'expResult': 2},
            {'orig': [1, 2, 1, 6, 3], 'expResult': 0}
        ]
        for x in testList:
            actResult = cb.arrayCount9(x['orig'])
            print '\nExpected: arrayCount9(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testArrayFront9(self):
        testList = [
            {'orig': [1, 2, 9, 3, 4], 'expResult': True},
            {'orig': [1, 2, 3, 4, 9], 'expResult': False},
            {'orig': [1, 2, 3, 4, 5], 'expResult': False},
            {'orig': [9, 2, 3], 'expResult': True},
            {'orig': [1, 2, 3], 'expResult': False},
            {'orig': [], 'expResult': False}
        ]
        for x in testList:
            actResult = cb.arrayFront9(x['orig'])
            print '\nExpected: arrayFront9(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testArray123(self):
        testList = [
            {'orig': [1, 1, 2, 3, 1], 'expResult': True},
            {'orig': [1, 1, 2, 4, 1], 'expResult': False},
            {'orig': [1, 2, 1, 2, 3], 'expResult': True},
            {'orig': [1, 2, 3, 1, 2, 3], 'expResult': True},
            {'orig': [1, 2, 3], 'expResult': True},
            {'orig': [2, 1], 'expResult': False},
            {'orig': [], 'expResult': False}
        ]
        for x in testList:
            actResult = cb.array123(x['orig'])
            print '\nExpected: array123(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testStringMatch(self):
        testList = [
            {'a': 'aabbccdd', 'b': 'abbbxxd', 'expResult': 1},
            {'a': 'abc', 'b': 'abc', 'expResult': 2},
            {'a': 'hello', 'b': 'he', 'expResult': 1},
            {'a': 'he', 'b': 'hello', 'expResult': 1},
            {'a': 'h', 'b': 'hello', 'expResult': 0},
            {'a': '', 'b': 'hello', 'expResult': 0},
            {'a': 'abc', 'b': 'axc', 'expResult': 0}
        ]
        for x in testList:
            actResult = cb.stringMatch(x['a'], x['b'])
            print '\nExpected: stringMatch(\'{a}\', \'{b}\') -> \'{expResult}\''.format(a=x['a'], b=x['b'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'

    def testCountEvens(self):
        testList = [
            {'orig': [1, 1, 2, 3, 1], 'expResult': 1},
            {'orig': [1, 1, 2, 4, 1], 'expResult': 2},
            {'orig': [1, 2, 3], 'expResult': 1},
            {'orig': [7, 1], 'expResult': 0},
            {'orig': [], 'expResult': 0}
        ]
        for x in testList:
            actResult = cb.countEvens(x['orig'])
            print '\nExpected: countEvens(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'



if __name__ == '__main__':
    unittest.main()