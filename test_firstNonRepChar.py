import unittest

import firstNonRepChar

class Test(unittest.TestCase):
    def test_first_non_rep_char_i(self):
        self.assertEqual(firstNonRepChar.main("ThisIsTheEnd"), I)
    def test_first_non_rep_char_o(self):
        self.assertEqual(firstNonRepChar.main("OneTwoOne"), o)
    def test_first_non_rep_char_no_rep(self):
        self.assertEqual(firstNonRepChar.main("NoReps"), 'No Repeats here!')

if __name__=='__main__':
    unittest.main()