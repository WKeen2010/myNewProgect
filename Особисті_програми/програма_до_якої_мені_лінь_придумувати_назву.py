from turtle import *
from random import *
fieldSize = 10
coordinates = []
accountant_list = []

speed(-1)
goto(20, -20)
clear()
for j in range(4):
    forward(fieldSize * 20)
    right(90)

def draw(x, y):
    up()
    goto(x * 20, -y * 20)
    down()
    color("black")
    begin_fill()
    for j in range(4):
        forward(20)
        right(90)
    end_fill()

def outline_x1(корабельні_палуби, x, y):
    i = coordinates.count(str(x + 1) + " | " + str(y - 1))
    if x + 1 < fieldSize + 1 and y - 1 > 0 and i == 0:
        coordinates.append(str(x + 1) + " | " + str(y - 1))
        draw(x + 1, y - 1,)
    d = 0
    for d in range(корабельні_палуби + 1):
        i = coordinates.count(str(x - d) + " | " + str(y - 1))
        if x - d > 0 and y - 1 > 0 and i == 0:
            coordinates.append(str(x - d) + " | " + str(y - 1))
            draw(x - d, y - 1)

    i = coordinates.count(str(x + 1) + " | " + str(y))
    if x + 1 < fieldSize + 1 and i == 0:
        coordinates.append(str(x + 1) + " | " + str(y))
        draw(x + 1, y)
    for d in range(корабельні_палуби + 1):
        i = coordinates.count(str(x - d) + " | " + str(y))
        if x - d > 0 and y - 1 > 0 and i == 0:
            coordinates.append(str(x - d) + " | " + str(y))
            draw(x - d, y)

    i = coordinates.count(str(x + 1) + " | " + str(y + 1))
    if x + 1 < fieldSize + 1 and y + 1 < fieldSize + 1 and i == 0:
        coordinates.append(str(x + 1) + " | " + str(y + 1))
        draw(x + 1, y + 1)
    d = 0
    for d in range(корабельні_палуби + 1):
        i = coordinates.count(str(x - d) + " | " + str(y + 1))
        if x - d > 0 and y + 1 < fieldSize + 1 and i == 0:
            coordinates.append(str(x - d) + " | " + str(y + 1))
            draw(x - d, y + 1)
def f():
    x, y = randint(1, 10), randint(1, 10)
    accountant_list.append(1)
    i = coordinates.count(str(x) + " | " + str(y))

    while i != 0:
        x, y = randint(1, 10), randint(1, 10)
        accountant_list.append(1)
        i = coordinates.count(str(x) + " | " + str(y))
    coordinates.append(str(x) + " | " + str(y))
    outline_x1(10, x, y)

    up()
    goto(x * 20, -y * 20)
    down()
    color("black")
    begin_fill()
    for j in range(4):
        forward(20)
        right(90)
    end_fill()

while len(coordinates) != 100:
    f()
print(len(accountant_list))

for k in range(360):
    left(1)