import last2
import string_bits
import unittest
import front_times
import string_splosion
import string_times

import codingBatWarmup2 as cb

__author__ = 'Jakub'

class TestHW2(unittest.TestCase):
    def testFrontTimes(self):
        testList = [
            {'orig': 'Chocolate', 'repeat': 3, 'expResult': 'ChoChoCho'},
            {'orig': 'Chocolate', 'repeat': 2, 'expResult': 'ChoCho'},
            {'orig': 'Abc', 'repeat': 3, 'expResult': 'AbcAbcAbc'},
            {'orig': 'Ab', 'repeat': 4, 'expResult': 'AbAbAbAb'},
            {'orig': 'A', 'repeat': 4, 'expResult': 'AAAA'},
            {'orig': '', 'repeat': 4, 'expResult': ''},
            {'orig': 'Abc', 'repeat': 0, 'expResult': ''},
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
            {'orig': '', 'repeat': 4, 'expResult': ''},
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
            {'orig': 'fade', 'expResult': 'ffafadfade'},
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
        ]
        for x in testList:
            actResult = cb.last2(x['orig'])
            print '\nExpected: stringBits(\'{orig}\') -> \'{expResult}\''.format(orig=x['orig'], expResult=x['expResult'])
            print 'Result: \'{actResult}\''.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)
        print '\n'




if __name__ == '__main__':
    unittest.main()