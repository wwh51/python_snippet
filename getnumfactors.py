import unittest
import time

def get_all_factors(x):
    factors = []
    factors.append(1)
    factors.append(x)
    i = 2
    mfactor = x
    while True:
        if x % i == 0:
            factors.append(i)
            mfactor = x // i
            if(mfactor > i):
                factors.append(mfactor)
        i += 1
        if(i >= mfactor):
            break
    return factors

def getnumfactors_slow(x):
    l=2
    i = 2
    mfactor = x
    while True:
        if x % i == 0:
            l += 1
            mfactor = x // i
            if(mfactor > i):
                l += 1
        i += 1
        if(i >= mfactor):
            break
    return l

def getnumfactors_fast(x):
    if x == 1 or x == 2:
        return x
    k = 0
    count = 1
    while(x&1 == 0):
        k += 1
        x = x>>1
    if x == 1:
        return k+1
    count += k
    i = 3
    while i*i <= x:
        k = 0
        while (x%i == 0):
            k += 1
            x = x // i
        count *= (k+1)
        i += 2
    if x > 1:
        count = count << 1
    return count


class TestGetnumfactors(unittest.TestCase):

    def setUp(self):
        pass

    def test_speed(self):
        t1=time.time()
        nstart = 7
        ntriangle = 28
        while True:
            if(getnumfactors_fast(ntriangle) > 200):
                break
            nstart += 1
            ntriangle += nstart
        res_1 = ntriangle
        t2=time.time()
        nstart = 7
        ntriangle = 28
        while True:
            if(getnumfactors_slow(ntriangle) > 200):
                break
            nstart += 1
            ntriangle += nstart
        t3 = time.time()
        self.assertEqual(ntriangle, res_1)
        self.assertLessEqual(t2-t1, t3-t2)
        # print(ntriangle)
        # print(t2-t1)
        # print(t3-t2)

if __name__ == '__main__':
    unittest.main()



