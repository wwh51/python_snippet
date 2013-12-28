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

    def test_reverse(self):
        a = list(range(10))
        self.assertEqual( a[::-1], list(reversed(a)))

    def test_flatten(self):
        self.assertEqual(list(range(1,9)),
            list(flatten([1, 2, [3, 4, [5, 6], 7], 8])) )

    def test_Infinite_Iterators(self):
        c = itertools.count(10,2)
        for i in range(10,20,2):
            self.assertEqual(i, next(c))
        self.assertEqual(20, next(c))

        #cycle('ABCD') --> A B C D A B C D ...
        c = list(itertools.repeat('dw',3))
        self.assertEqual(c, ['dw', 'dw', 'dw'])

    def test_Iterators(self):
        self.assertEqual(
            list(itertools.accumulate([1,2,3,4,5])),
            [1,3, 6, 10, 15]
         )
        self.assertEqual(
            list(itertools.chain('ABC', 'DEF')),
            ['A', 'B', 'C', 'D', 'E', 'F']
        )

        self.assertEqual(
            list(itertools.compress('ABCDEF', [1,0,1,0,1,1]) ),
            ['A', 'C', 'E', 'F']
        )

    def test_Combinatoric_generators(self):
        #product
        self.assertEqual(
            list(itertools.product([1,2],[3,4],[5,6])),
            [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]
        )
        self.assertEqual(
            list(itertools.product(  range(2), repeat=3  )),
            [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
        )

        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210
        self.assertEqual(
            [''.join(s) for s in itertools.permutations('ABCD', 2)],
            ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'CA', 'CB', 'CD', 'DA', 'DB', 'DC']
        )
        self.assertEqual(
            [''.join(s) for s in itertools.permutations('123')],
            ['123', '132', '213', '231', '312', '321']
        )

        self.assertEqual(
            [''.join(s) for s in itertools.combinations('ABCD', 2)],
            ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']
        )
        self.assertEqual(
            [''.join(s) for s in itertools.combinations_with_replacement('ABCD', 2)],
            ['AA', 'AB', 'AC', 'AD', 'BB', 'BC', 'BD', 'CC', 'CD', 'DD']
        )

        i= range(10)
        t=itertools.tee(i,3)
        a,b,c = next(t[0]), next(t[0]), next(t[0])
        self.assertEqual( (a,b,c), (0,1,2) )
        a,b,c = next(t[2]), next(t[2]), next(t[2])
        self.assertEqual( (a,b,c), (0,1,2) )
        a,b,c = next(t[0]), next(t[0]), next(t[0])
        self.assertEqual( (a,b,c), (3,4,5) )


if __name__== '__main__':
    unittest.main()
