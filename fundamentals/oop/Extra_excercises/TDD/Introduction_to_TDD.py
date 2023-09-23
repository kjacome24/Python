import unittest

def reverse_list (array):
    return array[::-1]

def isPalindrome(word):
    count = 0
    for i in range (len(word)):
        if word[i] == word[-i-1]:
            count += 1
        else:
            break
    if count == len(word):
        return True
    else:
        return False

class reverse_listtest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverse_list([1,3,5]), [5,3,1])
        self.assertTrue(isPalindrome ("racecar"))
        
    def testTwo(self):
        self.assertFalse(isPalindrome("rabcr"))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")


def factorial_con_recursion(n):
    if n == 1:
        return 1
    
    return n*factorial_con_recursion(n-1)

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas

