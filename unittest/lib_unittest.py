#test driven development
import unittest
import string #alphabet

def encrypt(message: str):
    #ecrypted_message = "".join([str(idx) for idx, char in enumerate(message)])
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    ecrypted_message = "".join([abc[abc.find(char)+1] if len(abc) > (abc.find(char)+1) else abc[0] for idx, char in enumerate(message)])
    return ecrypted_message

class TestEncryption(unittest.TestCase):
    #tests go here
    def setUp(self):
        self.my_message = "banana bread"
        
    #executes all funcs
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message) #if false(0) then PASSED
        
    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)#if my message is a string
    
    def test_funcReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))
        
    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))
    
    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message))
        
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str) #check that output is a string
    
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        ecrypted_message = "".join([abc[abc.find(char)+1] if len(abc) > (abc.find(char)+1) else abc[0] for idx, char in enumerate(self.my_message)])

        print(ecrypted_message)
        #print(abc[abc.find("c")+1])
        self.assertEqual(ecrypted_message, encrypt(self.my_message))
        
        
        
        
if __name__=="__main__":
    unittest.main()
