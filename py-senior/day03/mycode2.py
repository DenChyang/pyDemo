from functools import reduce

result = filter(lambda x: x % 2, [1, 2, 3, 4])
for tmp in result:
    print(tmp)
# print(result)

print("======")

demo = reduce(lambda x, y: str(x) + str(y), range(1, 101),"dd")
print(demo)
