n = int(input())
arr = []
for i in range(0,n):
    arr.append(input())
    
result = len(set(arr))
print(result)