import unittest

import helloWorld

class Test(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(helloWorld.Hello_World(), 'Hello, World!')

if __name__=='main':
    unittest.main()
