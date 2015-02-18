__author__ = 'Jakub'

import unittest
import front_times


class TestHW2(unittest.TestCase):
    def testFrontTimes(self):
        testList = [
            {'orig': 'Chocolate', 'repeat': 3, 'expResult': 'ChoChoCho'},
            {'orig': 'Chocolate', 'repeat': 2, 'expResult': 'ChoCho'},
            {'orig': 'xx', 'repeat': 3, 'expResult': 'xxxxxx'},
        ]
        for x in testList:
            actResult = front_times.frontTimes(x['orig'], x['repeat'])
            print '\n\nExpected: frontTimes(\'{orig}\', {repeat}) -> {expResult}'.format(orig=x['orig'], repeat=x['repeat'], expResult=x['expResult'])
            print 'Result: {actResult}'.format(actResult=actResult)
            self.assertEqual(x['expResult'], actResult)



if __name__ == '__main__':
    unittest.main()