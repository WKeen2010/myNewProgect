# Задача_Demo_A
a_x = int(input("Ax: "))
a_y = int(input("Ay: "))

b_x = int(input("Bx: "))
b_y = int(input("By: "))

c_x = int(input("Cx: "))
c_y = int(input("Cy: "))

d_x = int(input("Dx: "))
d_y = int(input("Dy: "))

if (a_x > c_x and a_x > d_x and b_x > d_x and b_x > d_x) or \
        (c_x > a_x and c_x > b_x and d_x > a_x and d_x > b_x):
    print(-1)

else:
    довжина_двох_проекцій = max(a_x, b_x, c_x, d_x) - min(a_x, b_x, c_x, d_x)
    частина_першої_проекції_яка_не_є_спільною = max(min(a_x, b_x), min(c_x, d_x)) - min(a_x, b_x, c_x, d_x)
    частина_другої_проекції_яка_не_є_спільною = max(a_x, b_x, c_x, d_x) - min(max(a_x, b_x), max(c_x, d_x))
    print(довжина_двох_проекцій - частина_першої_проекції_яка_не_є_спільною - частина_другої_проекції_яка_не_є_спільною)

# Задача_Demo_D
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

# Задача_Demo_E
n = input()
convert_n = list(n)
s = []
for i in range(len(convert_n)):
    if convert_n[i] == "1" or convert_n[i] == "2" or convert_n[i] == "3" or convert_n[i] == "1" or convert_n[i] == "4"or convert_n[i] == "5" or convert_n[i] == "6" or convert_n[i] == "7" or convert_n[i] == "8" or convert_n[i] == "9" or convert_n[i] == "0":
        s.append(convert_n[i])
print(s)

