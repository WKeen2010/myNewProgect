m = int(input())
n = int(input())
g =[]
key1 = False
key2 = False
s = 0

while m < n:
    g.append(m)
    m += 1

i = 0
for j in range(n - m):
    d = g.count(2 ** i)
    if d != 0:
        s += 1
    i += 1
print(s)