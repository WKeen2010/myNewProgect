from turtle import *

def f(x):
    for v in range(4):
        forward(x)
        left(90)

m = int(input('m = '))
n = int(input('n = '))

Matrix = [[input("M["+str(i)+"]["+str(j)+"]=") for j in range(n)] for i in range(m)]

print('')
print('Matrix:')

for i in range(m):
    print(Matrix[i])

for i in range(m):
    for j in range(n):
        if int(Matrix[i][j]) == 1:
            up()
            goto(j * 10, i * -10)
            down()
            begin_fill()
            f(10)
            end_fill()

for i in range(9999999):
    left(1)