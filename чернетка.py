from random import *

координати = []
збиті_кораблі = 0
палуби = 0

while збиті_кораблі < 20:

    пропуск1 = True
    пропуск2 = True
    пропуск3 = True
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
        координати.append(str(x) + str(y))
        координати.append(str(x - 1) + str(y - 1))
        координати.append(str(x) + str(y - 1))
        координати.append(str(x + 1) + str(y - 1))
        координати.append(str(x - 1) + str(y))
        координати.append(str(x + 1) + str(y))
        координати.append(str(x - 1) + str(y + 1))
        координати.append(str(x) + str(y + 1))
        координати.append(str(x + 1) + str(y + 1))
        continue

    elif f == "попав":
        збиті_кораблі += 1
        палуби += 1


        a = True
        x1 = x
        while a == True:
            x1 += 1
            i = координати.count(str(x1) + str(y))
            if x1 < 11 and i == 0:
                координати.append(str(x1) + str(y))
                print(x1, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    a = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск1 = False
                    пропуск2 = False
                    пропуск3 = False
                    if палуби == 2:
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

                    elif палуби == 3:
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

                    elif палуби == 4:
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

                elif f == "попав":
                    збиті_кораблі += 1
                    пропуск1 = False
                    пропуск2 = False
                    палуби += 1
                    continue
            else:
                a = False

        x2 = x
        while пропуск3 == True:
            x2 -= 1
            i = координати.count(str(x2) + str(y))
            if x2 > 0 and i == 0:
                координати.append(str(x2) + str(y))
                print(x2, " | ", y)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    пропуск3 = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск1 = False
                    пропуск2 = False
                    пропуск3 = False
                    if палуби == 2:
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

                    elif палуби == 3:
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

                    elif палуби == 4:
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

                elif f == "попав":
                    збиті_кораблі += 1
                    палуби += 1
                    пропуск1 = False
                    пропуск2 = False
                    continue
            else:
                пропуск3 = False

        y1 = y
        while пропуск1 == True:
            y1 += 1
            i = координати.count(str(x) + str(y1))
            if y1 < 11 and i == 0:
                координати.append(str(x) + str(y1))
                print(x, " | ", y1)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    пропуск1 = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск1 = False
                    if палуби == 2:
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y - 2))

                        координати.append(str(x) + str(y + 1))
                        координати.append(str(x) + str(y - 2))

                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y - 2))

                    elif палуби == 3:
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y - 2))
                        координати.append(str(x - 1) + str(y - 3))

                        координати.append(str(x) + str(y + 1))
                        координати.append(str(x) + str(y - 3))

                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y - 2))
                        координати.append(str(x + 1) + str(y - 3))

                    elif палуби == 4:
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y - 2))
                        координати.append(str(x - 1) + str(y - 3))
                        координати.append(str(x - 1) + str(y - 4))

                        координати.append(str(x) + str(y + 1))
                        координати.append(str(x) + str(y - 4))

                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y - 2))
                        координати.append(str(x + 1) + str(y - 3))
                        координати.append(str(x + 1) + str(y - 4))

            elif f == "попав":
                    збиті_кораблі += 1
                    палуби += 1
                    continue
            else:
                пропуск1 = False

        y2 = y
        while пропуск2 == True:
            y2 -= 1
            i = координати.count(str(x) + str(y2))
            if y2 > 0 and i == 0:
                координати.append(str(x) + str(y2))
                print(x, " | ", y2)
                f = input("(промах, попав, вбив): ")

                if f == "промах":
                    пропуск2 = False

                elif f == "вбив":
                    збиті_кораблі += 1
                    пропуск2 = False
                    if палуби == 2:
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y + 2))

                        координати.append(str(x) + str(y - 1))
                        координати.append(str(x) + str(y + 2))

                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y + 2))

                    elif палуби == 3:
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y + 2))
                        координати.append(str(x - 1) + str(y + 3))

                        координати.append(str(x) + str(y - 1))
                        координати.append(str(x) + str(y + 3))

                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y + 2))
                        координати.append(str(x + 1) + str(y + 3))

                    elif палуби == 4:
                        координати.append(str(x - 1) + str(y - 1))
                        координати.append(str(x - 1) + str(y))
                        координати.append(str(x - 1) + str(y + 1))
                        координати.append(str(x - 1) + str(y + 2))
                        координати.append(str(x - 1) + str(y + 3))
                        координати.append(str(x - 1) + str(y + 4))

                        координати.append(str(x) + str(y + 1))
                        координати.append(str(x) + str(y - 4))

                        координати.append(str(x + 1) + str(y - 1))
                        координати.append(str(x + 1) + str(y))
                        координати.append(str(x + 1) + str(y + 1))
                        координати.append(str(x + 1) + str(y + 2))
                        координати.append(str(x + 1) + str(y + 3))
                        координати.append(str(x + 1) + str(y + 4))

                elif f == "попав":
                    збиті_кораблі += 1
                    палуби += 1
                    continue
            else:
                пропуск2 = False
    палуби = 0

print("Кінець гри")
