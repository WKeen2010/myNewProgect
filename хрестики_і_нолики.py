move=1 # чий хід
x1=x2=x3=x4=x5=x6=x7=x8=x9=2
def field():
    print(x1,x2,x3)
    print(x4,x5,x6)
    print(x7,x8,x9)
#field()
k=0
winner=2
while k<9 and winner==2:
    field()
    print('Гравець ',move,', ваш хід')
    flag=True
    while flag:
        x=int(input())
        if x==1:
            if x1==2:
                flag=False
                x1=move
                if x2==move and x3==move:
                    winner=move
                if x4==move and x7==move:
                    winner=move
                if x5==move and x9==move:
                    winner=move
                elif x == 2:
                    if x2 == 2:
                        flag = False
                        x2 = move
                        if x1 == move and x3 == move:
                            winner = move
                        if x5 == move and x8 == move:
                            winner = move
                elif x == 3:
                    if x3 == 2:
                        flag = False
                        x3 = move
                        if x1 == move and x2 == move:
                            winner = move
                        if x6 == move and x9 == move:
                            winner = move
                        if x5 == move and x7 == move:
                            winner = move
                elif x == 4:
                    if x4 == 2:
                        flag = False
                        x4 = move
                        if x1 == move and x7 == move:
                            winner = move
                        if x5 == move and x6 == move:
                            winner = move
                elif x == 5:
                    if x5 == 2:
                        flag = False
                        x5 = move
                        if x4 == move and x6 == move:
                            winner = move
                        if x2 == move and x8 == move:
                            winner = move
                        if x1 == move and x9 == move:
                            winner = move
                        if x3 == move and x7 == move:
                            winner = move
                    elif x == 6:
                        if x6 == 2:
                            flag = False
                            x6 = move
                            if x4 == move and x5 == move:
                                winner = move
                            if x3 == move and x9 == move:
                                winner = move
                    elif x == 7:
                        if x7 == 2:
                            flag = False
                            x7 = move
                            if x1 == move and x4 == move:
                                winner = move
                            if x8 == move and x9 == move:
                                winner = move
                            if x3 == move and x5 == move:
                                winner = move
                    elif x == 8:
                        if x8 == 2:
                            flag = False
                            x8 = move
                            if x7 == move and x9 == move:
                                winner = move
                            if x2 == move and x5 == move:
                                winner = move
                    elif x == 9:
                        if x9 == 2:
                            flag = False
                            x9 = move
                            if x7 == move and x8 == move:
                                winner = move
                            if x3 == move and x6 == move:
                                winner = move
                            if x1 == move and x5 == move:
                                winner = move
                    move = 1 - move
                    k = k + 1
                field()
                print(winner, 'win')