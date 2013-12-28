import itertools
import unittest
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


class Test_itertoos(unittest.TestCase):
    def setup(self):
        pass

    def test_flatten(self):
        self.assertEqual(list(range(1,9)),
            list(flatten([1, 2, [3, 4, [5, 6], 7], 8])) )

    def test_Infinite_Iterators(self):
        c = itertools.count(10,2)
        for i in range(10,20,2):
            self.assertEqual(i, next(c))
        self.assertEqual(20, next(c))

        c = cycle('ABCD')

if __name__== '__main__':
    unittest.main()
