def getnumfactors(x):
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
