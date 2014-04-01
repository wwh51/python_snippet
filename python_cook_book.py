os.getcwd()
sys.path[0] == 'folder path of py file' # or sys.argv[0]

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record


from collections import deque
previous_lines = deque(maxlen=history)

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap)
heapq.heappush(heap, 100)

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d = defaultdict(set)

from collections import OrderedDict
d = OrderedDict() #preserves the original insertion order of data

min_price = min(zip(prices.values(), prices.keys()))

a.items() & b.items(); a.keys() & b.keys()

record = '....................100 .......513.25 ..........'
SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])


from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))

from operator import attrgetter
sorted(users, key=attrgetter('user_id')) # users is an object of class

from itertools import groupby
from operator import itemgetter
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date')) # important
for date, items in groupby(rows, key= lambda x : x['date']):
	print(date)
	for i in items:
		print(' ', i)

for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ', i)


addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
c = [a for i,a in enumerate(addresses) if counts[i] > 5]
# OR
from itertools import compress
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))


from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s.name == 'ACME'

t = [(1,2), (3,4), (5,6)]
list(itertools.chain(*t)) == list(itertools.chain(*t))
[item for t1 in t for item in t1]

(func1 if y == 1 else func2)(arg1, arg2) 
x = (class1 if y == 1 else class2)(arg1, arg2)

for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")
