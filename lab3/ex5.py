import functools

thelist = [(0, 2), (4, 3), (9, 9), (10, -1)]
values = []
result = []
for k, v in thelist: 
    #print(k, v)
    values.append(v)
#smallest = functools.reduce(lambda a, b: a if a < b else b, values)

while (len(thelist) != 0):
    smallest = functools.reduce(lambda a, b: a if a < b else b, values)
    values.remove(smallest)
    for k, v in thelist:
        if (v == smallest):
            result.append((k, v))
            thelist.remove((k, v))
print(result)