from random import *

координати = []
збиті_кораблі = 0

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
            координати.append(str(x1) + str(y))
            print(x1, " | ", y)
            f = input("(промах, попав, вбив): ")

            if f == "промах":
                a = False

            elif f == "вбив":
                збиті_кораблі += 1
                a = False

            elif f == "попав":
                збиті_кораблі += 1
                continue

        a = True
        x2 = x
        while a == True:
            x2 -= 1
            координати.append(str(x2) + str(y))
            print(x2, " | ", y)
            f = input("(промах, попав, вбив): ")

            if f == "промах":
                a = False

            elif f == "вбив":
                збиті_кораблі += 1
                a = False

            elif f == "попав":
                збиті_кораблі += 1
                continue

        a = True
        y1 = y
        while a == True:
            y1 += 1
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

        a = True
        y2 = y
        while a == True:
            y2 -= 1
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

print("Кінець гри")