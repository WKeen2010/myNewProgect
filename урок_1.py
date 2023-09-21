L=100.0
def f(x):
    global L
    return x*(L/2-x)
res=0
h=L/100.0
x=0
while x<=L/2:
    S=f(x)
    print(x,S)
    if S>res:
        res=S
    x=x+h
print(res)
