from random import *

координати = []
збиті_кораблі = 0


def shot_x(x, збиті_кораблі_x, e):
    a = True
    x1 = x
    while a == True:
        x1 = x1 + e
        if x1 < 11:
            координати.append(str(x1) + str(y))
            print(x1, " | ", y)
            f = input("(промах, попав, вбив): ")

            if f == "промах":
                a = False
                return збиті_кораблі_x

            elif f == "вбив":
                збиті_кораблі_x += 1
                пропуск = False
                a = False
                return збиті_кораблі_x

            elif f == "попав":
                збиті_кораблі_x += 1
                пропуск = False
                continue
        else:
            a = False
            return збиті_кораблі_x


def shot_y(y, збиті_кораблі_y, e):
    a = True
    y1 = y
    while a == True:
        y1 = y1 + e
        if y1 < 11:
            координати.append(str(x) + str(y1))
            print(x, " | ", y1)
            f = input("(промах, попав, вбив): ")

            if f == "промах":
                a = False
                return збиті_кораблі_y

            elif f == "вбив":
                збиті_кораблі_y += 1
                пропуск = False
                a = False
                return збиті_кораблі_y

            elif f == "попав":
                збиті_кораблі_y += 1
                пропуск = False
                continue
        else:
            a = False
            return збиті_кораблі_y


while збиті_кораблі < 20:

    x = randint(1,10)
    y = randint(1, 10)
    i = координати.count(str(x) + str(y))

    while i != 0:
        x = randint(1, 10)
        y = randint(1, 10)
        i = координати.count(str(x) + str(y))

    координати.append(str(x) + str(y))
    print(x, " | ", y)

    f = input("(промах, попав, вбив): ")
    if f == "промах":
        continue

    elif f == "вбив":
        збиті_кораблі += 1
        continue

    elif f == "попав":
        збиті_кораблі += 1

        збиті_кораблі += shot_x(x, збиті_кораблі, 1)

        збиті_кораблі += shot_x(x, збиті_кораблі, -1)

        збиті_кораблі += shot_x(x, збиті_кораблі, 1)

        збиті_кораблі += shot_x(x, збиті_кораблі, -1)

print("Кінець гри")