from turtle import *
from random import *

знищені_палуби = 0
кількість_палуб = 0

розмір_поля = 10
всього_палуб = 20
не_обстріляні_координати = []
for i in range(1, розмір_поля + 1):
    for j in range(1, розмір_поля + 1):
        не_обстріляні_координати.append(str(i) + "|" + str(j))

speed(-1)
goto(20, -20)
clear()
for o in range(4):
    forward(розмір_поля * 20)
    right(90)


def draw(x, y, type):
    up()
    goto(x * 20, -y * 20)
    down()
    if type == "промах":
        color("gray")
    elif type == "інше":
        color("black")
    begin_fill()
    for j in range(4):
        forward(20)
        right(90)
    end_fill()


def outline_x_right(корабельні_палуби, x, y):
    перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y - 1))
    if x < розмір_поля and y - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + 1) + "|" + str(y - 1))
        draw(x + 1, y - 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x - i) + "|" + str(y - 1))
        if x - i > 0 and y - 1 > 0 and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x - i) + "|" + str(y - 1))
            draw(x - i, y - 1, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y))
    if x < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + 1) + "|" + str(y))
        draw(x + 1, y, "промах")
    перевірка_значень = не_обстріляні_координати.count(str(x - корабельні_палуби) + "|" + str(y))
    if x - корабельні_палуби > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - корабельні_палуби) + "|" + str(y))
        draw(x - корабельні_палуби, y, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y + 1))
    if x < розмір_поля and y < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + 1) + "|" + str(y + 1))
        draw(x + 1, y + 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x - i) + "|" + str(y + 1))
        if x - i > 0 and y < розмір_поля and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x - i) + "|" + str(y + 1))
            draw(x - i, y + 1, "промах")



def outline_x_left(корабельні_палуби, x, y):
    перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y - 1))
    if x - 1 > 0 and y - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - 1) + "|" + str(y - 1))
        draw(x - 1, y - 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x + i) + "|" + str(y - 1))
        if x + i < розмір_поля + 1 and y - 1 > 0 and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x + i) + "|" + str(y - 1))
            draw(x + i, y - 1, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y))
    if x - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - 1) + "|" + str(y))
        draw(x - 1, y, "промах")
    перевірка_значень = не_обстріляні_координати.count(str(x + корабельні_палуби) + "|" + str(y))
    if x + корабельні_палуби < розмір_поля + 1 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + корабельні_палуби) + "|" + str(y))
        draw(x + корабельні_палуби, y, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y + 1))
    if x - 1 > 0 and y < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - 1) + "|" + str(y + 1))
        draw(x - 1, y + 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x + i) + "|" + str(y + 1))
        if x + i < розмір_поля + 1 and y < розмір_поля and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x + i) + "|" + str(y + 1))
            draw(x + i, y + 1, "промах")



def outline_y_down(корабельні_палуби, x, y):
    перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y + 1))
    if y < розмір_поля and x - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - 1) + "|" + str(y + 1))
        draw(x - 1, y + 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y - i))
        if y - i > 0 and x - 1 > 0 and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x - 1) + "|" + str(y - i))
            draw(x - 1, y - i, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x) + "|" + str(y + 1))
    if y < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x) + "|" + str(y + 1))
        draw(x, y + 1, "промах")
    перевірка_значень = не_обстріляні_координати.count(str(x) + "|" + str(y - корабельні_палуби))
    if y - корабельні_палуби > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x) + "|" + str(y - корабельні_палуби))
        draw(x, y - корабельні_палуби, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y + 1))
    if x < розмір_поля and y < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + 1) + "|" + str(y + 1))
        draw(x + 1, y + 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y - i))
        if y - i > 0 and x < розмір_поля and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x + 1) + "|" + str(y - i))
            draw(x + 1, y - i, "промах")


def outline_y_up(корабельні_палуби, x, y):
    перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y - 1))
    if x - 1 > 0 and y - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x - 1) + "|" + str(y - 1))
        draw(x - 1, y - 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x - 1) + "|" + str(y + i))
        if x - 1 > 0 and y + i < розмір_поля + 1 and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x - 1) + "|" + str(y + i))
            draw(x - 1, y + i, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x) + "|" + str(y - 1))
    if y - 1 > 0 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x) + "|" + str(y - 1))
        draw(x, y - 1, "промах")
    перевірка_значень = не_обстріляні_координати.count(str(x) + "|" + str(y + корабельні_палуби))
    if y + корабельні_палуби < розмір_поля + 1 and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x) + "|" + str(y + корабельні_палуби))
        draw(x, y + корабельні_палуби, "промах")

    перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y - 1))
    if y - 1 > 0 and x < розмір_поля and перевірка_значень != 0:
        не_обстріляні_координати.remove(str(x + 1) + "|" + str(y - 1))
        draw(x + 1, y - 1, "промах")
    i = 0
    for i in range(корабельні_палуби + 1):
        перевірка_значень = не_обстріляні_координати.count(str(x + 1) + "|" + str(y + i))
        if y + i < розмір_поля + 1 and x < розмір_поля and перевірка_значень != 0:
            не_обстріляні_координати.remove(str(x + 1) + "|" + str(y + i))
            draw(x + 1, y + i, "промах")


while знищені_палуби < всього_палуб:

    дозвіл_на_биття_по_y_down = True
    дозвіл_на_биття_по_y_up = True
    дозвіл_на_биття_по_x_left = True
    дозвіл_на_биття_по_x_right = True

    координати = choice(не_обстріляні_координати)
    не_обстріляні_координати.remove(координати)
    x = ""
    кількість_цифр = 0
    while координати[кількість_цифр] != "|":
        x = x + координати[кількість_цифр]
        кількість_цифр = кількість_цифр + 1
    x = int(x)
    y = list(координати)
    for g in range(кількість_цифр + 1):
        y.pop(0)
    y = int("".join(y))
    print(x, " | ", y)

    f = input("(промах, попав, вбив): ")
    if f == "промах":
        draw(x, y, "промах")
        continue

    elif f == "вбив":
        знищені_палуби += 1
        draw(x, y, "інше")
        outline_x_right(1, x, y)
        continue

    elif f == "попав":
        знищені_палуби += 1
        кількість_палуб += 1
        draw(x, y, "інше")


        x_right = x
        while дозвіл_на_биття_по_x_right == True:
            x_right += 1
            i = не_обстріляні_координати.count(str(x_right) + "|" + str(y))
            if x_right < розмір_поля + 1 and i != 0:
                не_обстріляні_координати.remove(str(x_right) + "|" + str(y))
                print(x_right, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    дозвіл_на_биття_по_x_right = False
                    draw(x_right, y, "промах")

                elif f == "вбив":
                    знищені_палуби += 1
                    дозвіл_на_биття_по_y_down = False
                    дозвіл_на_биття_по_y_up = False
                    дозвіл_на_биття_по_x_left = False
                    дозвіл_на_биття_по_x_right = False
                    кількість_палуб += 1
                    draw(x_right, y, "інше")
                    outline_x_right(кількість_палуб, x_right, y)

                elif f == "попав":
                    знищені_палуби += 1
                    дозвіл_на_биття_по_y_down = False
                    дозвіл_на_биття_по_y_up = False
                    кількість_палуб += 1
                    draw(x_right, y, "інше")
                    continue

                if не_обстріляні_координати.count(str(x_right) + "|" + str(y)) != 0:
                    не_обстріляні_координати.remove(str(x_right) + "|" + str(y))
            else:
                дозвіл_на_биття_по_x_right = False

        x_left = x
        while дозвіл_на_биття_по_x_left == True:
            x_left -= 1
            i = не_обстріляні_координати.count(str(x_left) + "|" + str(y))
            if x_left > 0 and i != 0:
                print(x_left, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    дозвіл_на_биття_по_x_left = False
                    draw(x_left, y, "промах")

                elif f == "вбив":
                    знищені_палуби += 1
                    дозвіл_на_биття_по_y_down = False
                    дозвіл_на_биття_по_y_up = False
                    дозвіл_на_биття_по_x_left = False
                    кількість_палуб += 1
                    draw(x_left, y, "інше")
                    outline_x_left(кількість_палуб, x_left, y)

                elif f == "попав":
                    знищені_палуби += 1
                    кількість_палуб += 1
                    дозвіл_на_биття_по_y_down = False
                    дозвіл_на_биття_по_y_up = False
                    draw(x_left, y, "інше")
                    continue
                if не_обстріляні_координати.count(str(x_left) + "|" + str(y)) != 0:
                    не_обстріляні_координати.remove(str(x_left) + "|" + str(y))
            else:
                дозвіл_на_биття_по_x_left = False

        y_down = y
        while дозвіл_на_биття_по_y_down == True:
            y_down += 1
            i = не_обстріляні_координати.count(str(x) + "|" + str(y_down))
            if y_down < розмір_поля + 1 and i != 0:
                не_обстріляні_координати.remove(str(x) + "|" + str(y_down))
                print(x, " | ", y_down)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    дозвіл_на_биття_по_y_down = False
                    draw(x, y_down, "промах")

                elif f == "вбив":
                    знищені_палуби += 1
                    дозвіл_на_биття_по_y_down = False
                    дозвіл_на_биття_по_y_up = False
                    кількість_палуб += 1
                    draw(x, y_down, "інше")
                    outline_y_down(кількість_палуб, x, y_down)

                elif f == "попав":
                        знищені_палуби += 1
                        кількість_палуб += 1
                        draw(x, y_down, "інше")
                        continue
                if не_обстріляні_координати.count(str(x) + "|" + str(y_down)) != 0:
                    не_обстріляні_координати.remove(str(x) + "|" + str(y_down))
            else:
                дозвіл_на_биття_по_y_down = False

        y_up = y
        while дозвіл_на_биття_по_y_up == True:
            y_up -= 1
            i = не_обстріляні_координати.count(str(x) + "|" + str(y_up))
            if y_up > 0 and i != 0:
                не_обстріляні_координати.remove(str(x) + "|" + str(y_up))
                print(x, " | ", y_up)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    дозвіл_на_биття_по_y_up = False
                    draw(x, y_up, "промах")

                elif f == "вбив":
                    знищені_палуби += 1
                    дозвіл_на_биття_по_y_up = False
                    кількість_палуб += 1
                    draw(x, y_up, "інше")
                    outline_y_up(кількість_палуб, x, y_up)

                elif f == "попав":
                    знищені_палуби += 1
                    кількість_палуб += 1
                    draw(x, y_up, "інше")
                    continue
                if не_обстріляні_координати.count(str(x) + "|" + str(y_up)) != 0:
                    не_обстріляні_координати.remove(str(x) + "|" + str(y_up))
            else:
                дозвіл_на_биття_по_y_up = False
    else:
        print("Ти грав неправильно!")
        break
    кількість_палуб = 0

print("Кінець гри")

for k in range(999999):
    left(1)