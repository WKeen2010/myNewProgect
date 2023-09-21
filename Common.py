a, b, c = map(str, input().split())
d = 0
for i in range(len(max(a, b, c))):
    if a[0] == b[0] or a[0] == b[1] or a[0] == b[2] or a[0] == b[3] or a[0] == b[4] or a[0] == b[5] or a[1] == b[0]\
            or a[1] == b[1] or a[1] == b[2] or a[1] == b[3] or a[1] == b[4] or \
            a[1] == b[5] or a[2] == b[0] or a[2] == b[1] or a[2] == b[2] or a[2] == b[3] or \
            a[2] == b[4] or a[2] == b[5] or a[3] == b[0] or a[3] == b[1] or a[3] == b[2] \
            or a[3] == b[3] or a[3] == b[4] or a[3] == b[5] or a[4] == b[0] or a[4] == b[1] or a[4] == b[2]\
            or a[4] == b[3] or a[4] == b[4] or a[4] == b[5] or a[5] == b[0] or a[5] == b[1] or \
            a[5] == b[2] or a[5] == b[3] or a[5] == b[4] or a[5] == b[5]:
        if a[0] == c[0] or a[0] == c[1] or a[0] == c[2] or a[0] == c[3]\
                or a[1] == c[0] or a[1] == c[1] or a[1] == c[2] or a[1] == c[3] or a[2] == c[0] or a[2] == c[1]\
                or a[2] == c[2] or a[2] == c[3] or a[3] == c[0] or a[3] == c[1] or a[3] == c[2] or a[3] == c[3]:
            d = d + 1

print(int(d / 2))