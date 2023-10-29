n = int(input(""))
a = []
for i in range(n):
    x_s, y_s, r_s, x_m, y_m, r_m = map(int, input().split())
    if x_s == x_m and y_s == y_m and r_s <= r_m:
        a.append("3")
    elif x_s == x_m and y_s == y_m and r_s > r_m:
        a.append("2")
    elif (r_s + r_m) > (abs(x_s - x_m)) and (r_s + r_m) > (abs(y_s - y_m)):
        a.append("1")
    elif (r_s + r_m) < (abs(x_s - x_m)) or (r_s + r_m) < (abs(y_s - y_m)):
        a.append("0")
print(a)