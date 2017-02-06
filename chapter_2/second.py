x = [4,1,2,3]
y = sorted(x)
x.sort()

x = sorted([-4,1,-2,3], key=abs, reverse=True)

word_counts = {('test', 1), ('test2', 3)}

#wc = sorted(word_counts.items(),
#            key=lambda (word,count) : count,
#            reverse=True)

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

square_dict = { x : x * x for x in range(5) }

pairs = [(x, y)
         for x in range(10)
         for y in range(10)]

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


lazy_evens_below_20 = (i for i in xrange(20) if i % 2 == 0 )

#for x in lazy_evens_below_20:
#    print x

import random

four_uniform_randoms = [random.random() for _ in range(4)]

random.randrange(10)
random.randrange(3, 6)

up_to_ten = range(10)

random.shuffle(up_to_ten)

my_best_friend = random.choice(['John', 'Pelle', 'Therese'])

lotery_numbers = range(60)
six_winner_numbers = random.sample(lotery_numbers, 6)

four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]

import re
all([
    not re.match('a', 'cat'),
    re.search('a', 'cat'),
    not re.search('c', 'dog'),
    3 == len(re.split('[ab]', 'carbs')),
    "R-D-" == re.sub('[0-9]', '-', 'R2D2')
])

class Set:

    def __init__(self, values=None):

        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([1,2,3])
s.add(6)
s.remove(3)

def exp(base, power):
    return base ** power

def two_to_the(power):
    return exp(2, power)

print two_to_the(3)

from functools import partial
two_to_the = partial(exp, 2)

square_of = partial(exp, power=2)
print square_of(3)

def double(x):
    return x*2

xs = [1,2,3,4]

twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)


def multiply(x, y):
    return x*y

multi_xs = map(multiply, xs, xs)

def is_even(x):
    return x % 2 == 0

even_xs = filter(is_even, xs)
even_xs = [x for x in xs if is_even(x)]
list_evener = partial(filter, is_even)
even_xs = list_evener(xs)

x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)


documents = ['','','']

# Bad
for i in range(len(documents)):
    document = documents[i]
    #do_something(i, document)

# Also bad
i = 0
for document in documents:
    #do_something(i, document)
    i += 1

for i, document in enumerate(documents):
    print i
    print document
    #do_something(i, document)

for i, _ in enumerate(documents): print i#do_something(i)

