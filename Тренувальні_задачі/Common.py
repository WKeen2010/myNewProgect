a, b, c = map(list, input().split())
n = 0
i = 0

for i in range(10):
    if a.count(str(i)) != 0 and b.count(str(i)) != 0 and c.count(str(i)) != 0:
        n += 1

print(n)