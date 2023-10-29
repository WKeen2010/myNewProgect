primary_n = input()
n_a = list(primary_n)
n_b = list(primary_n)

a = []
b = []

convert_n_a = n_a
for i in range(len(n_a)):
    a.append(str(min(convert_n_a)))
    convert_n_a.remove(min(convert_n_a))

convert_n_b = n_b
for i in range(len(n_b)):
    b.append(str(max(convert_n_b)))
    convert_n_b.remove(max(convert_n_b))

print(a)
print(b)