def vector_add(v, w):
    return [x + y
            for x,y in zip(v, w)]

def vector_subract(v, w):
    return [vi - wi
            for vi, wi in zip(v, w)]

def vector_sum(vectors):
    #result = vectors[0]
    #for vector in vectors[1:]:
    #    result = vector_add(result, vector)
    return reduce(vector_add, vectors)

print vector_add([1,2],[2,3])
print vector_subract([1,2],[2,3])

vectors = [[1,1],[2,2],[3,3]]

print vector_sum(vectors)
