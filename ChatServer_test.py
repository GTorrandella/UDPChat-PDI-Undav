import unittest
import unittest.mock
import GaboProtocol as gp

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
        s1, s2 = gp.prepareMessage("Hello World!")
        b1 = "12".encode(encoding='utf_8', errors='strict')
        b2 = "Hello World!".encode(encoding='utf_8', errors='strict')
        
        self.assertEqual(s1, b1)
        self.assertEqual(s2, b2)
        
    def test_sendMessage(self):
        pass
    
    def test_recvMessage(self):
        pass
    
if __name__ == '__main__':
    unittest.main()