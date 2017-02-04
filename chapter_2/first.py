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


