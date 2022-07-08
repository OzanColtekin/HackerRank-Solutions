import numpy

inp = input().split(" ")
n,m = int(inp[0]), int(inp[1])

array = []

for _ in range(n): array.append(list(map(int, input().split())))
array = numpy.array(array)
print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))