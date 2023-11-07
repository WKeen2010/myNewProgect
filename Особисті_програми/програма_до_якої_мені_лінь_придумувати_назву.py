from turtle import *
from random import *
fieldSize = 10
coordinates = []
accountant_list = []

for i in range(fieldSize):
    for j in range(fieldSize):
        coordinates.append(str(i) + str(j))

speed(-1)
for d in range(4):
    forward(fieldSize * 20)
    right(90)

def draw(x, y):
    up()
    goto(x * 20, -y * 20)
    down()
    color("black")
    begin_fill()
    for s in range(4):
        forward(20)
        right(90)
    end_fill()

def f():
    a = choice(coordinates)
    accountant_list.append(1)
    coordinates.remove(a)
    x = int(a[0])
    y = int(a[1])
    draw(x, y)


while len(coordinates) != 0:
    f()
print(len(accountant_list))

for k in range(360):
    left(1)