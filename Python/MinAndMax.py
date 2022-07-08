import numpy

inp = input().split(" ")
n,m = int(inp[0]), int(inp[1])

array = []

for i in range(n): 
    array.append(list(map(int,input().split(" "))))

result = numpy.min(array, axis=1)
print(numpy.max(result))