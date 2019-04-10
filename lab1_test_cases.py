import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_2(self):
        self.assertEqual(max_list_iter([]),None)

    def test_max_list_iter_3(self):
        self.assertEqual(max_list_iter([1,3,3]),3)

    def test_max_list_iter_4(self):
        self.assertEqual(max_list_iter([6,2,3]),6)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_2(self):
        self.assertEqual(reverse_rec([1,2,3,4,5]),[5,4,3,2,1])

    def test_reverse_rec_3(self):
        self.assertEqual(reverse_rec([1,2]),[2,1])

    def test_reverse_rec_4(self):
        self.assertEqual(reverse_rec([3]),[3])

    def test_reverse_rec_5(self):
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )

if __name__ == "__main__":
        unittest.main()

    
