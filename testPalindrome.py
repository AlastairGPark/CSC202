import unittest
from Palindrome import delims
from Palindrome import isPalindrome

class TestStacks(unittest.TestCase):
    
    def testleft(self) -> None:
        self.assertTrue(delims(''))

    def testsame(self) -> None:
        self.assertTrue(delims('()'))

    def testmismatch(self) -> None:
        self.assertTrue(delims('(}'))

    def testi(self) -> None:
        self.assertEqual(isPalindrome('I'), True)

    def testeye(self) -> None:
        self.assertEqual(isPalindrome('eye'), True)

    def testabba(self) -> None:
        self.assertEqual(isPalindrome('Abba'), True)

    def testhannah(self) -> None:
        self.assertEqual(isPalindrome('Hannah'), True)

    def testmadam(self) -> None:
        self.assertEqual(isPalindrome("Madam, I'm Adam"), True)

    def testaman(self) -> None:
        self.assertEqual(isPalindrome('A man, a plan, a canal: Panama!'), True)

    def testalastair(self) -> None:
        self.assertEqual(isPalindrome('Alastair'), False)

    def testgarfield(self) -> None:
        self.assertEqual(isPalindrome('Garfield'), False)

    def testpark(self) -> None:
        self.assertEqual(isPalindrome('Park'), False)

    def testbaba(self) -> None:
        self.assertEqual(isPalindrome('baba'), False)

if __name__ == '__main__':
    unittest.main()