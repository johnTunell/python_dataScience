
from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0
#for word in document:
#    word_counts[word] += 1



dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: [1]}
dd_dict = defaultdict(dict) # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle" # { "Joel" : { "City" : Seattle"}}
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0,1]}


test_dict = defaultdict(int)

print test_dict[2]

test_dict[4] = 1

print test_dict

def pairMatch(arr, sum):
    dict = defaultdict(int)
    for value in arr:
        if dict[sum - value] is 1:
            return sum - value, value
        else:
            dict[value] = 1
    return ()



print pairMatch([4,1,2,4,5], 3)





