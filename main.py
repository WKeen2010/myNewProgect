m = int(input('m = '))
n = int(input('n = '))
s = []
a = 0

Matrix = [[input("M["+str(i)+"]["+str(j)+"]=") for j in range(n)] for i in range(m)]

print('')
print('Matrix:')

for i in range(m):
    print(Matrix[i])

for i in range(m):
    for j in range(n):
        if int(Matrix[i][j]) == 1:
            s = s + [i, j]

while a == 0:

    if abs(s[0] - s[2]) < 2 and abs(s[1] - s[3]) < 2:
        del s[0], s[1]

        if len(s) / 2 == 1:
            a = 1

        else:
            a = 0

    else:

        if len(s) >= 5:
            if abs(s[0] - s[4]) < 2 and abs(s[1] - s[5]) < 2:
                del s[0], s[1]

                if len(s) / 2 == 1:
                    a = 1

                else:
                    a = 0

            else:
                a = len(s) / 2

        else:
            a = len(s) / 2

print('')
print(a)