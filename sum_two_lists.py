a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x: x[0] + x[1], zip(a, b)))
print(result)