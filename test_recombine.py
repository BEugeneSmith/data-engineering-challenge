import unittest
from recombine import Recombine

class TestRecombine(unittest.TestCase):

    test_dict = '[ { "a":1, "b":2 }, { "b":3, "c":4 }, { "c":6, "a":5 } ]'
    test_list = '[ ["a","b","c"], [1,2,null], [null,3,4], [5,null,6] ]'
    test_json = '{"a": [1, null, 5], "b": [2, 3, null], "c": [null, 4, 6]}'


    def test_recombineList(self):
        rtest_list = Recombine(self.test_list)
        self.assertEqual(rtest_list.json,self.test_json)

    def test_recombineDict(self):
        rtest_dict = Recombine(self.test_dict)
        self.assertEqual(rtest_dict.json,self.test_json)

if __name__ == '__main__':
    unittest.main()
