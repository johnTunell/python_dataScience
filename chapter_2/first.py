def double(x):
    return x*x

def apply_to_one(f):
    return f(2)

six = apply_to_one(lambda x: x + 4)

def my_print(message = "my default message"):
    print message

def subtract(a = 1, b = 1):
    return a - b


multi_line_strint = """This is the first line.
and this is the second line
and this is the thied line"""

try:
    print 0/0
except ZeroDivisionError:
    print "cannot divide by zero"


integer_list = [1,2,3,4,5,6,7,8,9]
heterogeneous_list = ["strng", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

zero_to_seven = range(8)
seven = zero_to_seven[-1]
zero_to_three = zero_to_seven[:4]
four_to_end = zero_to_seven[4:]
three_to_five = zero_to_seven[3:6]
copy = zero_to_seven[:]

1 in [1,2,3]
0 in [1,2,3]

x = [1,2,3]
x.extend([4,5,6])

y = x + [4,5,6]
x.append(0)

a, b = [1,2]
_, b = [1,2]

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 1,2
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"

def sum_and_product(x, y):
    return x+y, x*y

s, p = sum_and_product(2, 3)

x, y = 1, 2
x, y = y, x

empty_dict = {}
empty_dict2 = dict()
john = "john"

grades = { "Joel" : 80, "Tim" : 95, john: 8}

try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

# Default value. Cool
joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)

grades["Joel"] = 99

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet.keys()
tweet.values()
tweet.items()

test_dict = {
    ('key', 'pair') : 2
}


"user" in tweet
"joelgrus" in tweet.values()

document = ['hej']
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in document:
   previous_count = word_counts.get(word, 0)
   word_counts[word] = previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle" # dict() produces an empty dict
# { "Joel" : { "City" : Seattle"}}
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0,1]}

from collections import Counter

c = Counter([0, 1, 2, 0])
document = ['hej', 'da','da','haja']
word_counts = Counter(document)

for word, count in word_counts.most_common(10):
    print word, count

s = set()
s.add(1)
s.add(2)
s.add(2)

item_list = [1,2,3,1,2,3]
num_items = len(item_list)
item_set = set(item_list)

x = 2
parity = "even" if x % 2 == 0 else "odd"

#for x in range(10):
    #print x, "is less than 10"

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print x

x = None
y = "Something"
print x == None
print x is None
print y is "Something"

def some_function_that_returns_a_string():
    return "a string"

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ''

first_char = s and s[0]

safe_x = x or 0

all([True, 1, {3}])
all([True, 1, {}])
any([True, 1, {}])
all([])
any([])




