from random import *

координати = []
збиті_кораблі = 0
check = []

def checker_x(a, b):
    координати_x = []
    if len(a) == 1:
        координати.append(str(x-1) + str(y-1))
        координати.append(str(x) + str(y-1))
        координати.append(str(x+1) + str(y-1))

        координати.append(str(x-1) + str(y))
        координати.append(str(x+1) + str(y))

        координати.append(str(x-1) + str(y+1))
        координати.append(str(x) + str(y+1))
        координати.append(str(x+1) + str(y+1))

    elif len(a) == 2 and b == 1:
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x + 2) + str(y - 1))

        координати.append(str(x - 1) + str(y))
        координати.append(str(x + 2) + str(y))

        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x + 2) + str(y + 1))

    elif len(a) == 2 and b == 2:
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x - 2) + str(y - 1))

        координати.append(str(x + 1) + str(y))
        координати.append(str(x - 2) + str(y))

        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x - 2) + str(y + 1))

    elif len(a) == 3 and b == 1:
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x + 2) + str(y - 1))
        координати.append(str(x + 3) + str(y - 1))

        координати.append(str(x - 1) + str(y))
        координати.append(str(x + 3) + str(y))

        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x + 2) + str(y + 1))
        координати.append(str(x + 3) + str(y + 1))

    elif len(a) == 3 and b == 2:
        координати.append(str(x - 2) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x + 2) + str(y - 1))

        координати.append(str(x - 2) + str(y))
        координати.append(str(x + 2) + str(y))

        координати.append(str(x - 2) + str(y + 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x + 2) + str(y + 1))

    elif len(a) == 3 and b == 3:
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x - 2) + str(y - 1))
        координати.append(str(x - 3) + str(y - 1))

        координати.append(str(x + 1) + str(y))
        координати.append(str(x - 3) + str(y))

        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x - 2) + str(y + 1))
        координати.append(str(x - 3) + str(y + 1))

    elif len(a) == 4 and b == 1:
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x + 2) + str(y - 1))
        координати.append(str(x + 3) + str(y - 1))
        координати.append(str(x + 4) + str(y - 1))

        координати.append(str(x - 1) + str(y))
        координати.append(str(x + 4) + str(y))

        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x + 2) + str(y + 1))
        координати.append(str(x + 3) + str(y + 1))
        координати.append(str(x + 4) + str(y + 1))

    elif len(a) == 4 and b == 2:
        координати.append(str(x - 2) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x + 2) + str(y - 1))
        координати.append(str(x + 3) + str(y - 1))

        координати.append(str(x - 2) + str(y))
        координати.append(str(x + 3) + str(y))

        координати.append(str(x - 2) + str(y + 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x + 2) + str(y + 1))
        координати.append(str(x + 3) + str(y + 1))

    elif len(a) == 4 and b == 3:
        координати.append(str(x + 2) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x - 2) + str(y - 1))
        координати.append(str(x - 3) + str(y - 1))

        координати.append(str(x - 3) + str(y))
        координати.append(str(x + 2) + str(y))

        координати.append(str(x + 2) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x - 2) + str(y + 1))
        координати.append(str(x - 3) + str(y + 1))

    elif len(a) == 4 and b == 4:
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x - 2) + str(y - 1))
        координати.append(str(x - 3) + str(y - 1))
        координати.append(str(x - 4) + str(y - 1))

        координати.append(str(x + 1) + str(y))
        координати.append(str(x - 4) + str(y))

        координати.append(str(x + 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x - 2) + str(y + 1))
        координати.append(str(x - 3) + str(y + 1))
        координати.append(str(x - 4) + str(y + 1))

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


        a = True
        x1 = x
        while a == True:
            x1 += 1
            if x1 < 11:
                координати.append(str(x1) + str(y))
                print(x1, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    a = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск = False
                    a = False

                elif f == "попав":
                    збиті_кораблі += 1
                    пропуск = False
                    continue
            else:
                a = False

        a = True
        x2 = x
        while a == True:
            пропуск = False
            x2 -= 1
            if x2 > 0:
                координати.append(str(x2) + str(y))
                print(x2, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    a = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск = False
                    a = False

                elif f == "попав":
                    збиті_кораблі += 1
                    пропуск = False
                    continue
            else:
                a = False

        y1 = y
        while пропуск == True:
            y1 += 1
            if y1 < 11:
                координати.append(str(x) + str(y1))
                print(x, " | ", y1)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    a = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    a = False

                elif f == "попав":
                    збиті_кораблі += 1
                    continue
            else:
                a = False

        y2 = y
        while пропуск == True:
            y2 -= 1
            if y2 > 0:
                координати.append(str(x) + str(y2))
                print(x, " | ", y2)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    a = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    a = False

                elif f == "попав":
                    збиті_кораблі += 1
                    continue
            else:
                a = False

print("Кінець гри")