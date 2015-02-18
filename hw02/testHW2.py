__author__ = 'Jakub'

import unittest
import front_times


class TestHW2(unittest.TestCase):
    def testFrontTimes(self):
        orig = 'Chocolate'
        repeat = 3
        expResult = 'ChoChoCho'
        actResult = front_times.frontTimes(orig, repeat)
        print '\n\nExpected: frontTimes(\'{orig}\', {repeat}) -> {expResult}'.format(orig=orig, repeat=repeat, expResult=expResult)
        print 'Result: {actResult}'.format(actResult=actResult)
        self.assertEqual(expResult, actResult)


if __name__ == '__main__':
    unittest.main()