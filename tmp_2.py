from random import *


координати = []
m = 10    # РОЗМІРИ
n = 10    # ПОЛЯ
кількість_знищених_кораблів = 0
порядок = 0

while кількість_знищених_кораблів < 20:

    x = randint(1, 10)
    y = randint(1, 10)
    i = координати.count(str(x) + str(y))

    while i != 0:
        x = randint(1, 10)
        y = randint(1, 10)
        i = координати.count(str(x) + str(y))

    print(x, '|', y)
    координати.append(str(x) + str(y))
    f = input('(Промах, попав, вбив)')
    if f == 'Промах':
        continue
    elif f == 'вбив':
        кількість_знищених_кораблів += 1
    elif f == 'попав':
        кількість_знищених_кораблів += 1

        порядок = 0
        x1 = x
        x1 = x1 + 1
        координати.append(str(x1) + str(y))
        print(x1, '|', y)
        f = input('(Промах, попав, вбив)')
        if f == 'вбив':
            кількість_знищених_кораблів += 1
        elif f == 'попав':
            x1 = x1 + 1
            порядок = 0
            while порядок < 4 or кількість_знищених_кораблів < 20:
                координати.append(str(x1) + str(y))
                print(x1, '|', y)
                f = input('(Промах, попав, вбив)')
                if f == 'Промах':
                    порядок = 4
                    break
                elif f == 'вбив':
                    кількість_знищених_кораблів += 1
                    break
                elif f == 'попав':
                    x1 += 1
                    кількість_знищених_кораблів += 1
                    порядок = 0
                    x1 = x1 + 1
                    координати.append(str(x1) + str(y))
                    print(x1, '|', y)
                    f = input('(Промах, попав, вбив)')
                    if f == 'вбив':
                        кількість_знищених_кораблів += 1
                    elif f == 'попав':
                        x1 = x1 + 1
                        порядок = 0
                        while порядок < 4 or кількість_знищених_кораблів < 20:
                            координати.append(str(x1) + str(y))
                            print(x1, '|', y)
                            f = input('(Промах, попав, вбив)')
                            if f == 'Промах':
                                порядок = 4
                                break
                            elif f == 'вбив':
                                кількість_знищених_кораблів += 1
                                break
                            elif f == 'попав':
                                x1 += 1
                                кількість_знищених_кораблів += 1
                                порядок = 0
                                x1 = x1 + 1
                                координати.append(str(x1) + str(y))
                                print(x1, '|', y)
                                f = input('(Промах, попав, вбив)')
                                if f == 'вбив':
                                    кількість_знищених_кораблів += 1
                                elif f == 'попав':
                                    x1 = x1 + 1
                                    порядок = 0
                                    while порядок < 4 or кількість_знищених_кораблів < 20:
                                        координати.append(str(x1) + str(y))
                                        print(x1, '|', y)
                                        f = input('(Промах, попав, вбив)')
                                        if f == 'Промах':
                                            порядок = 4
                                            break
                                        elif f == 'вбив':
                                            кількість_знищених_кораблів += 1
                                            break
                                        elif f == 'попав':
                                            x1 += 1
                                            кількість_знищених_кораблів += 1
                                            порядок = 0
                                            x1 = x1 + 1
                                            координати.append(str(x1) + str(y))
                                            print(x1, '|', y)
                                            f = input('(Промах, попав, вбив)')
                                            if f == 'вбив':
                                                кількість_знищених_кораблів += 1
                                            elif f == 'попав':
                                                x1 = x1 + 1
                                                порядок = 0
                                                while порядок < 4 or кількість_знищених_кораблів < 20:
                                                    координати.append(str(x1) + str(y))
                                                    print(x1, '|', y)
                                                    f = input('(Промах, попав, вбив)')
                                                    if f == 'Промах':
                                                        порядок = 4
                                                        break
                                                    elif f == 'вбив':
                                                        кількість_знищених_кораблів += 1
                                                        break
                                                    elif f == 'попав':
                                                        x1 += 1
                                                        кількість_знищених_кораблів += 1

        порядок = 0
        x2 = x
        x2 = x2 - 1
        координати.append(str(x2) + str(y))
        print(x2, '|', y)
        f = input('(Промах, попав, вбив)')
        if f == 'вбив':
            кількість_знищених_кораблів += 1
        elif f == 'попав':
            координати.append(str(x2) + str(y))
            x2 = x2 - 1
            порядок = 0
            while порядок < 4 or кількість_знищених_кораблів < 20:
                x2 = x2 - 1
                координати.append(str(x2) + str(y))
                print(x2, '|', y)
                f = input('(Промах, попав, вбив)')
                if f == 'Промах':
                    порядок = 4
                    break
                elif f == 'вбив':
                    кількість_знищених_кораблів += 1
                    break
                elif f == 'попав':
                    x2 = x2 - 1
                    кількість_знищених_кораблів += 1
                    порядок = 0
                    x2 = x2 - 1
                    координати.append(str(x2) + str(y))
                    print(x2, '|', y)
                    f = input('(Промах, попав, вбив)')
                    if f == 'вбив':
                        кількість_знищених_кораблів += 1
                    elif f == 'попав':
                        x2 = x2 - 1
                        порядок = 0
                        while порядок < 4 or кількість_знищених_кораблів < 20:
                            x2 = x2 - 1
                            координати.append(str(x2) + str(y))
                            print(x2, '|', y)
                            f = input('(Промах, попав, вбив)')
                            if f == 'Промах':
                                порядок = 4
                                break
                            elif f == 'вбив':
                                кількість_знищених_кораблів += 1
                                break
                            elif f == 'попав':
                                x2 = x2 - 1
                                кількість_знищених_кораблів += 1
                                порядок = 0
                                x2 = x2 - 1
                                координати.append(str(x2) + str(y))
                                print(x2, '|', y)
                                f = input('(Промах, попав, вбив)')
                                if f == 'вбив':
                                    кількість_знищених_кораблів += 1
                                elif f == 'попав':
                                    x2 = x2 - 1
                                    порядок = 0
                                    while порядок < 4 or кількість_знищених_кораблів < 20:
                                        x2 = x2 - 1
                                        координати.append(str(x2) + str(y))
                                        print(x2, '|', y)
                                        f = input('(Промах, попав, вбив)')
                                        if f == 'Промах':
                                            порядок = 4
                                            break
                                        elif f == 'вбив':
                                            кількість_знищених_кораблів += 1
                                            break
                                        elif f == 'попав':
                                            x2 = x2 - 1
                                            кількість_знищених_кораблів += 1
                                            порядок = 0
                                            x2 = x2 - 1
                                            координати.append(str(x2) + str(y))
                                            print(x2, '|', y)
                                            f = input('(Промах, попав, вбив)')
                                            if f == 'вбив':
                                                кількість_знищених_кораблів += 1
                                            elif f == 'попав':
                                                x2 = x2 - 1
                                                порядок = 0
                                                while порядок < 4 or кількість_знищених_кораблів < 20:
                                                    x2 = x2 - 1
                                                    координати.append(str(x2) + str(y))
                                                    print(x2, '|', y)
                                                    f = input('(Промах, попав, вбив)')
                                                    if f == 'Промах':
                                                        порядок = 4
                                                        break
                                                    elif f == 'вбив':
                                                        кількість_знищених_кораблів += 1
                                                        break
                                                    elif f == 'попав':
                                                        x2 = x2 - 1
                                                        кількість_знищених_кораблів += 1

        порядок = 0
        y1 = y
        y1 = y1 + 1
        координати.append(str(x) + str(y1))
        print(x, '|', y1)
        f = input('(Промах, попав, вбив)')
        if f == 'вбив':
            кількість_знищених_кораблів += 1
        elif f == 'попав':
            y1 += 1
            порядок = 0
            while порядок < 4 or кількість_знищених_кораблів < 20:
                y1 = y1 + 1
                координати.append(str(x) + str(y1))
                print(x, '|', y1)
                f = input('(Промах, попав, вбив)')
                if f == 'Промах':
                    порядок = 4
                    break
                elif f == 'вбив':
                    кількість_знищених_кораблів += 1
                    break
                elif f == 'попав':
                    y1 += 1
                    кількість_знищених_кораблів += 1
                    порядок = 0
                    координати.append(str(x) + str(y1))
                    print(x, '|', y1)
                    f = input('(Промах, попав, вбив)')
                    if f == 'вбив':
                        кількість_знищених_кораблів += 1
                    elif f == 'попав':
                        y1 += 1
                        порядок = 0
                        while порядок < 4 or кількість_знищених_кораблів < 20:
                            y1 = y1 + 1
                            координати.append(str(x) + str(y1))
                            print(x, '|', y1)
                            f = input('(Промах, попав, вбив)')
                            if f == 'Промах':
                                порядок = 4
                                break
                            elif f == 'вбив':
                                кількість_знищених_кораблів += 1
                                break
                            elif f == 'попав':
                                y1 += 1
                                кількість_знищених_кораблів += 1
                                порядок = 0
                                координати.append(str(x) + str(y1))
                                print(x, '|', y1)
                                f = input('(Промах, попав, вбив)')
                                if f == 'вбив':
                                    кількість_знищених_кораблів += 1
                                elif f == 'попав':
                                    y1 += 1
                                    порядок = 0
                                    while порядок < 4 or кількість_знищених_кораблів < 20:
                                        y1 = y1 + 1
                                        координати.append(str(x) + str(y1))
                                        print(x, '|', y1)
                                        f = input('(Промах, попав, вбив)')
                                        if f == 'Промах':
                                            порядок = 4
                                            break
                                        elif f == 'вбив':
                                            кількість_знищених_кораблів += 1
                                            break
                                        elif f == 'попав':
                                            y1 += 1
                                            кількість_знищених_кораблів += 1
                                            порядок = 0
                                            координати.append(str(x) + str(y1))
                                            print(x, '|', y1)
                                            f = input('(Промах, попав, вбив)')
                                            if f == 'вбив':
                                                кількість_знищених_кораблів += 1
                                            elif f == 'попав':
                                                y1 += 1
                                                порядок = 0
                                                while порядок < 4 or кількість_знищених_кораблів < 20:
                                                    y1 = y1 + 1
                                                    координати.append(str(x) + str(y1))
                                                    print(x, '|', y1)
                                                    f = input('(Промах, попав, вбив)')
                                                    if f == 'Промах':
                                                        порядок = 4
                                                        break
                                                    elif f == 'вбив':
                                                        кількість_знищених_кораблів += 1
                                                        break
                                                    elif f == 'попав':
                                                        y1 += 1
                                                        кількість_знищених_кораблів += 1

        порядок = 0
        y2 = y
        y2 = y2 + 1
        координати.append(str(x) + str(y2))
        print(x, '|', y2)
        f = input('(Промах, попав, вбив)')
        if f == 'вбив':
            кількість_знищених_кораблів += 1
        elif f == 'попав':
            y2 += 1
            порядок = 0
            while порядок < 4 or кількість_знищених_кораблів < 20:
                y2 = y2 + 1
                координати.append(str(x) + str(y2))
                print(x, '|', y2)
                f = input('(Промах, попав, вбив)')
                if f == 'Промах':
                    порядок = 4
                    break
                elif f == 'вбив':
                    кількість_знищених_кораблів += 1
                    break
                elif f == 'попав':
                    y2 += 1
                    кількість_знищених_кораблів += 1
                    порядок = 0
                    координати.append(str(x) + str(y2))
                    print(x, '|', y2)
                    f = input('(Промах, попав, вбив)')
                    if f == 'вбив':
                        кількість_знищених_кораблів += 1
                    elif f == 'попав':
                        y2 += 1
                        порядок = 0
                        while порядок < 4 or кількість_знищених_кораблів < 20:
                            y2 = y2 + 1
                            координати.append(str(x) + str(y2))
                            print(x, '|', y2)
                            f = input('(Промах, попав, вбив)')
                            if f == 'Промах':
                                порядок = 4
                                break
                            elif f == 'вбив':
                                кількість_знищених_кораблів += 1
                                break
                            elif f == 'попав':
                                y2 += 1
                                кількість_знищених_кораблів += 1
                                порядок = 0
                                координати.append(str(x) + str(y2))
                                print(x, '|', y2)
                                f = input('(Промах, попав, вбив)')
                                if f == 'вбив':
                                    кількість_знищених_кораблів += 1
                                elif f == 'попав':
                                    y2 += 1
                                    порядок = 0
                                    while порядок < 4 or кількість_знищених_кораблів < 20:
                                        y2 = y2 + 1
                                        координати.append(str(x) + str(y2))
                                        print(x, '|', y2)
                                        f = input('(Промах, попав, вбив)')
                                        if f == 'Промах':
                                            порядок = 4
                                            break
                                        elif f == 'вбив':
                                            кількість_знищених_кораблів += 1
                                            break
                                        elif f == 'попав':
                                            y2 += 1
                                            кількість_знищених_кораблів += 1
                                            порядок = 0
                                            координати.append(str(x) + str(y2))
                                            print(x, '|', y2)
                                            f = input('(Промах, попав, вбив)')
                                            if f == 'вбив':
                                                кількість_знищених_кораблів += 1
                                            elif f == 'попав':
                                                y2 += 1
                                                порядок = 0
                                                while порядок < 4 or кількість_знищених_кораблів < 20:
                                                    y2 = y2 + 1
                                                    координати.append(str(x) + str(y2))
                                                    print(x, '|', y2)
                                                    f = input('(Промах, попав, вбив)')
                                                    if f == 'Промах':
                                                        порядок = 4
                                                        break
                                                    elif f == 'вбив':
                                                        кількість_знищених_кораблів += 1
                                                        break
                                                    elif f == 'попав':
                                                        y2 += 1
                                                        кількість_знищених_кораблів += 1

print('кінець гри')