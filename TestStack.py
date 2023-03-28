import unittest

from Stack import Stack

class TestStack(unittest.Testcase):
    def setUp(self) -> None:
        self.empty: Stack[int] = Stack[int]()

        self._1item: Stack[int] = Stack[int]()
        self._1item.push(5)

        self._3items: Stack[str] = Stack[str]()
        self._3items.push(42)
        self._3items.push(600)
        self._3items.push(7)

    def test_empty(self) -> None:
        self.assertTrue(self.empty.empty())
        self.assertFalse(self._1item.empty())
        self.assertFalse(self._3items.empty())

    def testPush(self) -> None:
        self._empty.push(314)
        self.assertFalse(self._empty.empty())
        self.assertEqual(self._empty.pop(), 314)
        self.assertTrue(self._empty.empty())

    def testPushNonEmpty(self) -> None:
        self.assertEqual(self._1item.peek(), 5)
        self.push(12)
        self.assertEqual(self._1item.pop(), 12)
        self.asserEqual(self._1item.pop(), 5)
        self.assertTrue(self._1item.empty())

    def testPop(self) -> None:
        with self.assertRaises(AssertionError):
            self.empty.pop()
        self.assertEqual(self._1item.pop(), 5)
        self.assertTrue(self._1item.empty())
        self.assertEqual(self._3items.pop(), 7)
        self.assertEqual(self._3items.pop(), 600)
        self.assertEqual(self._3items.pop(), 42)
        self.assertTrue(self._3items.empty())
    
    def testMatchedDelimiters(self) -> None:
        # Obvious False Cases
        self.assertFalse(matched_delimiters('('))
        self.assertFalse(matched_delimiters('['))
        self.assertFalse(matched_delimiters('{'))
        self.assertFalse(matched_delimiters(')'))
        self.assertFalse(matched_delimiters(']'))
        self.assertFalse(matched_delimiters('}'))
        self.assertFalse(matched_delimiters("'"))
        self.assertFalse(matched_delimiters('"'))
        self.assertFalse(matched_delimiters('`'))
        self.assertFalse(matched_delimiters('%'))
        self.assertFalse(matched_delimiters('$'))

        #Obvious True Cases
        self.assertTrue(matched_delimiters('()'))
        self.assertTrue(matched_delimiters('[]'))
        self.assertTrue(matched_delimiters('{}'))
        self.assertFalse(matched_delimiters("'"))
        self.assertFalse(matched_delimiters('""'))
        self.assertFalse(matched_delimiters('``'))
        self.assertFalse(matched_delimiters('$$'))
        self.assertFalse(matched_delimiters('%%'))

        #Nesting
        self.assertTrue(matched_delimiters('(()()()())'))
        self.assertTrue(matched_delimiters('(((())))'))

if __name__ == '__main__':
    unittest.main()