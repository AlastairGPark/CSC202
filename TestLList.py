# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from LList import LList

class TestNothing(unittest.TestCase):
    def setUp(self) -> None:
        self._empty: LList[str] = LList[str]()

        self._1item: LList[str] = LList[str]()
        self._1item.add('Strider')

        self._2items: LList[str] = LList[str]()
        self._2items.add('Pollux')
        self._2items.add('Castor')

        self._3items: LList[str] = LList[str]()
        self._3items.add('Moe')
        self._3items.add('Curly')
        self._3items.add('Larry')



    # All methods whose names start with "test"
    # will be treated as tests
    def test_empty(self) -> None:
        self.assertTrue(self._empty.is_empty())
        self.assertFalse(self._1item.is_empty())

    def test_str(self) -> None:
        self.assertEqual(str(self._empty), '∅')
        self.assertEqual(str(self._1item), '❬Strider❭➞∅')

    def test_add(self) -> None:
        self.assertEqual(str(self._1item), '❬Strider❭➞∅')
        self.assertEqual(str(self._2items), '❬Castor❭➞❬Pollux❭➞∅')
        self.assertEqual(str(self._3items), '❬Larry❭➞❬Curly❭➞❬Moe❭➞∅')

    def test_size(self) -> None:
        self.assertEqual(self._empty.size(), 0)
        self.assertEqual(self._1item.size(), 1)
        self.assertEqual(self._2items.size(), 2)
        self.assertEqual(self._3items.size(), 3)

    def test_len(self) -> None:
        self.assertEqual(len(self._empty), 0)
        self.assertEqual(len(self._1item), 1)
        self.assertEqual(len(self._2items), 2)
        self.assertEqual(len(self._3items), 3)

    def test_search(self) -> None:
        self.assertFalse(self._empty.search('Strider'))
        self.assertFalse(self._1item.search('Castor'))
        self.assertFalse(self._2items.search('Strider'))
        self.assertFalse(self._3items.search('Strider'))
        self.assertTrue(self._1item.search('Strider'))
        self.assertTrue(self._2items.search('Castor'))
        self.assertTrue(self._2items.search('Pollux'))
        self.assertTrue(self._3items.search('Larry'))
        self.assertTrue(self._3items.search('Curly'))
        self.assertTrue(self._3items.search('Moe'))

    def test_contains(self) -> None:
        self.assertFalse('Strider' in self._empty)
        self.assertFalse('Castor' in self._1item)
        self.assertFalse('Strider' in self._2items)
        self.assertFalse('Strider' in self._3items)
        self.assertTrue('Strider' in self._1item)
        self.assertTrue('Castor' in self._2items)
        self.assertTrue('Pollux' in self._2items)
        self.assertTrue('Larry' in self._3items)
        self.assertTrue('Curly' in self._3items)
        self.assertTrue('Moe' in self._3items)

    def test_pop(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop(0)
        with self.assertRaises(AssertionError):
            self._1item.pop(1)
        with self.assertRaises(AssertionError):
            self._1item.pop(-2)
        self.assertEqual(self._1item.pop(0), 'Strider')
        self.assertTrue(self._1item.is_empty())
        self.assertEqual(self._2items.pop(-1), 'Pollux')
        self.assertEqual(self._2items.size(), 1)
        self.assertEqual(self._2items.pop(0), 'Castor')
        self.assertTrue(self._2items.is_empty())
        self.assertEqual(self._3items.pop(-2), 'Curly')
        self.assertEqual(self._3items.size(), 2)
        self.assertEqual(self._3items.pop(1), 'Moe')
        self.assertEqual(self._3items.size(), 1)
        self.assertEqual(self._3items.pop(-1), 'Larry')
        self.assertTrue(self._3items.is_empty())

if __name__ == '__main__':
    unittest.main()
