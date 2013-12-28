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

        self.assertEqual(
            list( itertools.dropwhile(lambda x: x<5, [1,4,6,4,1])  ),
            [6,4,1]
        )

        self.assertEqual(
            list( itertools.takewhile(lambda x: x<5, [1,4,6,4,1])  ),
            [1,4]
        )

        self.assertEqual(
            list(filter(lambda x:x%2, range(10) ) ),
            [1, 3, 5, 7, 9]
        )

        self.assertEqual(
            list(itertools.filterfalse(lambda x:x%2, range(10) ) ),
            [0, 2, 4, 6, 8]
        )

        self.assertEqual(
            list(itertools.islice(range(100), 10,70,10)), #seq, [start,] stop [, step]
            [10, 20, 30, 40, 50, 60]
        )

        self.assertEqual(
            list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')),
            [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]
            )

        self.assertEqual(
            list(itertools.starmap(pow, [(2,5), (3,2), (10,3)]) ),
            [32, 9, 1000]
        )

        groups = []
        uniquekeys = []
        keyfunc = lambda x: x%3
        data = list(range(20))
        data = sorted(data, key=keyfunc)
        for k, g in itertools.groupby(data, keyfunc):
           groups.append(list(g))
           uniquekeys.append(k)
        self.assertEqual(uniquekeys, [0, 1, 2])
        self.assertEqual(groups,
            [[0, 3, 6, 9, 12, 15, 18], [1, 4, 7, 10, 13, 16, 19], [2, 5, 8, 11, 14, 17]])


        i= range(10)
        t=itertools.tee(i,3)
        a,b,c = next(t[0]), next(t[0]), next(t[0])
        self.assertEqual( (a,b,c), (0,1,2) )
        a,b,c = next(t[2]), next(t[2]), next(t[2])
        self.assertEqual( (a,b,c), (0,1,2) )
        a,b,c = next(t[0]), next(t[0]), next(t[0])
        self.assertEqual( (a,b,c), (3,4,5) )

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

if __name__== '__main__':
    unittest.main()
