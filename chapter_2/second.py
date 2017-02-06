x = [4,1,2,3]
y = sorted(x)
print y
print x
x.sort()
print x

x = sorted([-4,1,-2,3], key=abs, reverse=True)
print(x)

word_counts = {('test', 1), ('test2', 3)}

#wc = sorted(word_counts.items(),
#            key=lambda (word,count) : count,
#            reverse=True)

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
print squares
