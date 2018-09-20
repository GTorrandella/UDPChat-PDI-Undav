import unittest
import GaboProtocol as gp
from builtins import int

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_countBytes(self):
        s = gp.countBytes("Hello World!")
        b = "12".encode(encoding='utf_8', errors='strict')
        
        self.assertEqual(s, b)
        
    def test_prepareMessage(self):
        
    def test_sendMessage(self):
    
    def test_recvMessage(self):

if __name__ == '__main__':
    unittest.main()