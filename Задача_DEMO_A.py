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